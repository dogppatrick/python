import glob
import numpy as np
import pandas as pd
from datetime import date, time, datetime
from keras.models import load_model


def model_selector(flower, week, type_model):
    if type_model == 0:
        arr = np.array(pd.read_csv("./flower_pre_model/01_model/result_best.csv"))
    else:
        arr = np.array(pd.read_csv("./flower_pre_model/04_model/result_best.csv"))
    # flower,week ="Anthurium",1
    shift2 = (week - 1) * 7 + 1
    sample = arr[(arr[:, 0] == flower) * (arr[:, 3] == shift2)][0]
    key = "_".join(sample[:4].astype(str))

    if type_model == 0:
        fn = glob.glob("./flower_pre_model/01_model/" + key + ".h5")[0]
    else:
        fn = glob.glob("./flower_pre_model/04_model/" + key + "_c4.h5")[0]
    model_info = sample
    return fn, model_info


def prep_rdata(r_data):
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
    return r_data


def trans_z(r_data, station):
    recordz = pd.read_csv("./flower_pre_model/weather_trans.csv")
    mean_trans = np.array(recordz[station][0].replace("[", "").replace("]", "").replace(" ", "").split(",")).astype(float)
    std_trans = np.array(recordz[station][1].replace("[", "").replace("]", "").replace(" ", "").split(",")).astype(float)
    col_x = r_data.columns.to_list()
    for i in range(len(col_x)):
        r_data[col_x[i]] = (r_data[col_x[i]] - [mean_trans[i]]) / std_trans[i]
    return r_data


def shift_rdata(r_data, shift1):
    df_s = r_data.copy()
    arr_all = np.array(df_s)
    for i in range(1, shift1):
        tp = np.array(df_s.shift(periods=i))
        arr_all = np.concatenate((arr_all, tp), axis=1)
    df_all = pd.DataFrame(arr_all)
    df_all = df_all.dropna()
    df_all = df_all.reset_index(drop=True)
    return df_all


def get_week(pre_date):
    d_date = pre_date
    year = int(d_date.split("-")[0])
    d_day = date(year, int(d_date.split("-")[1]), int(d_date.split("-")[2])) - date(year, 1, 1)
    return 1 + (d_day.days // 7)


def model_predict(market, pre_date, flower, week_pre, type_model=0):
    fn, model_info = model_selector(flower, week_pre, type_model)
    flower, station, shift1, shift2, test_acc, train_acc = model_info
    fn_weather= glob.glob("../result/merge_weather/" + station + "*.csv")[0]
    df_weather = pd.read_csv(fn_weather, encoding="utf-8")
    df_lunar = pd.read_csv("../lunar_done_new.csv", encoding="utf-8")
    d_data =  list(df_weather["Date"])
    weather = prep_rdata(df_weather)
    weather_z = trans_z(weather,station)
    weather_z["date"]= d_data
    x_join = weather_z.join(df_lunar.set_index("date"), on="date").drop(columns="date")
    start_index = d_data.index(pre_date)
    x_join = x_join[(start_index-shift1-shift2):(start_index-shift2)]
    x_shift = shift_rdata(x_join, shift1)
    x = list(x_shift.reset_index(drop=True).iloc[0])
    week = get_week(pre_date)
    mark_list = ["台中", "台北", "台南", "彰化", "高雄"]
    add_mark = [0, 0, 0, 0, 0]
    add_mark[mark_list.index(market)] = 1
    add_week = [0]*52
    add_week[(week-1)] = 1
    x = x + add_mark + add_week
    x_res = np.array(x).reshape(1, len(x))
    model = load_model(fn)
    if type_model == 0:
        result_tag = ["跌", "漲"]
    else:
        result_tag = ["大跌", "小跌", "小漲", "大漲"]
    return result_tag[model.predict_classes(x_res)[0]]

