import pandas as pd
import numpy as np
from glob import glob
# 指定要更新的資料夾
st_list = ["467480", "C0F9L0", "C0K490", "C0X060"]
# 更新的天氣資訊放的位置
p_dir = "../raw_weather/weather_update_0531/"
# 主要天氣資訊放的位置
main_weather_dir = "../result/merge_weather/"


def update_weather_data(p_dir, station_name):
    data_file = glob(p_dir + "//*" + station_name + "*.csv")
    df_all = pd.DataFrame()
    n = len(data_file)
    for i in range(n):
        fn_load = data_file[i]
        df_tmp = pd.read_csv(fn_load,encoding="utf-8",
                             names=['Date', 'Temperature', 'T.Max', 'T.Min', 'Precp',
                                    'RH', 'StnPres', 'WS', 'WSGust'])
        if i == 0:
            df_all = df_tmp
        else:
            df_all = df_all.append(df_tmp)
    df_all = df_all.reset_index()
    df_all = df_all.drop(columns="index")
    df_all = df_all.dropna(axis=0)
    return df_all


for station_name in st_list:
    update_data = update_weather_data(p_dir, station_name)
    main_data_fn = glob(main_weather_dir + "*" + station_name + "*.csv")[0]
    main_data = pd.read_csv(main_data_fn)
    merger_data  = main_data.append(update_data)
    merger_data.drop_duplicates(subset="Date")
    main_data_fn = main_data_fn.replace(".csv", "") + ".csv"
    merger_data.to_csv(main_data_fn,encoding="utf-8", index=False)
    print(station_name, "updated")

