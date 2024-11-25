import os
import pandas as pd

# 设置文件夹路径
folder_path = '/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/acorn_sat_v2.4.0_daily_tmean'

# 遍历文件夹中的所有CSV文件
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        # 读取CSV文件
        data = pd.read_csv(file_path)
        # 检查重复行
        duplicate_rows = data.duplicated().sum()
        # 输出重复数据的信息
        if duplicate_rows > 0:
            print(f"{filename} has {duplicate_rows} duplicate rows.")
        else:
            print(f"{filename} has no duplicate rows.")
