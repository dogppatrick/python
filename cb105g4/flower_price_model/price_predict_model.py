import glob
import numpy as np
import pandas as pd
from datetime import date, datetime, timedelta
from keras.models import load_model
import os

class PPModel:
    def __init__(self, market, pre_date, flower, week, type_mode=0):
        self.dir_path = os.path.abspath('.')
        self.market = market
        self.pre_date = datetime.strptime(pre_date, "%Y-%m-%d").date()
        self.add_w = (self.pre_date - date(self.pre_date.year, 1, 1)).days // 7
        self.flower = flower
        self.week = week  # 使用幾周前的資料做預測 1,2,3 >[1,8,15]
        self.type_mode = type_mode  # 漲跌 / 大小 * 漲跌
        self.model_selector()
        self.fn_weather = glob.glob(self.dir_path + "/weather/" + self.station + "*.csv")[0]
        self.r_data = pd.read_csv(self.fn_weather, encoding="utf-8")  # r_data >>天氣資訊/變形
        self.df_lunar = pd.read_csv(self.dir_path + "/lunar_done_new.csv", encoding="utf-8")
        self.d_data = list(self.r_data["Date"])
        self.prep_rdata()
        self.trans_z()
        self.join_weather()
        self.shift_x()
        self.select_x()
        if (self.x_sel.shape[0] == 0):
            print("氣象資訊不足/選擇錯誤,需更新天氣資訊")
        self.add_week_marker()

    #         天氣 + 節慶資訊

    def model_selector(self):
        #         決定使用哪種model >> 讀取不同檔案
        flower = self.flower
        week = self.week
        if self.type_mode == 0:
            arr = np.array(pd.read_csv(self.dir_path + "/01_model/result_best.csv"))
        else:
            arr = np.array(pd.read_csv(self.dir_path + "/04_model/result_best.csv"))
        # flower,week ="Anthurium",1
        shift2 = (week - 1) * 7 + 1
        sample = arr[(arr[:, 0] == flower) * (arr[:, 3] == shift2)][0]
        key = "_".join(sample[:4].astype(str))

        if self.type_mode == 0:
            fn = glob.glob(self.dir_path + "01_model/" + key + ".h5")[0]
        else:
            fn = glob.glob(self.dir_path + "/04_model/" + key + "_c4.h5")[0]
        model_info = sample
        self.fn = fn
        self.model_info = model_info
        flower, self.station, self.shift1, self.shift2, test_acc, train_acc = model_info

    def prep_rdata(self):
        r_data = self.r_data
        col_fix = ['T.Max', 'T.Min', 'Precp', 'Temperature', 'RH', 'StnPres', 'WS', 'WSGust']
        for col in col_fix:
            old = r_data[col]
            new = []
            for i in range(len(old)):
                try:
                    new.append(float(old[i]))
                    tmp = float(old[i])
                except ValueError:
                    new.append(tmp)
            r_data[col] = new
        d_tmp = r_data['T.Max'] - r_data['T.Min']
        r_data["d_tmp"] = d_tmp
        drop_c = ["Date", 'T.Max', 'T.Min']
        r_data = r_data.drop(columns=drop_c)
        self.r_data = r_data

    def trans_z(self):
        r_data = self.r_data
        station = self.station
        recordz = pd.read_csv(self.dir_path + "/weather_trans.csv")
        mean_trans = np.array(recordz[station][0].replace("[", "").replace("]", "").replace(" ", "").split(",")).astype(
            float)
        std_trans = np.array(recordz[station][1].replace("[", "").replace("]", "").replace(" ", "").split(",")).astype(
            float)
        col_x = r_data.columns.to_list()
        for i in range(len(col_x)):
            r_data[col_x[i]] = (r_data[col_x[i]] - [mean_trans[i]]) / std_trans[i]
        self.r_data = r_data

    def join_weather(self):
        self.r_data["date"] = self.d_data
        self.x_join = self.r_data.join(self.df_lunar.set_index("date"), on="date").drop(columns="date")

    def shift_x(self):
        x_join = self.x_join
        shift1 = self.shift1
        df_s = x_join.copy()
        arr_all = np.array(df_s)
        for i in range(1, shift1):
            tp = np.array(df_s.shift(periods=i))
            arr_all = np.concatenate((arr_all, tp), axis=1)
        df_all = pd.DataFrame(arr_all)
        df_all["date"] = self.d_data
        df_all = df_all.dropna()
        df_all = df_all.reset_index(drop=True)
        self.x_join = df_all

    def select_x(self):
        sel_d = self.pre_date - timedelta(days=1 + ((self.week - 1) * 7))
        self.x_sel = self.x_join[self.x_join["date"] == datetime.strftime(sel_d, "%Y-%m-%d")]

    def add_week_marker(self):
        self.x = list(self.x_sel.iloc[0])[:-1]
        mark_list = ["台中", "台北", "台南", "彰化", "高雄"]
        add_mark = [0] * 5
        add_mark[mark_list.index(self.market)] = 1
        add_week = [0] * 52
        add_week[(self.add_w - 1)] = 1
        self.x = self.x + add_mark + add_week
        self.x = np.array(self.x).reshape(1, len(self.x))

    def result(self):
        model = load_model(self.fn)
        if self.type_mode == 0:
            result_tag = ["跌", "漲"]
        else:
            result_tag = ["大跌", "小跌", "小漲", "大漲"]
        return result_tag[model.predict_classes(self.x)[0]]



