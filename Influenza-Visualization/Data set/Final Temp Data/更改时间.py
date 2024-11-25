import pandas as pd
import os

# 设置包含所有气象站CSV文件的文件夹路径
directory = '/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/untitled folder/process data'

# 遍历文件夹中的所有文件
for filename in os.listdir(directory):
    if filename.endswith('.csv'):  # 确保处理的是CSV文件
        file_path = os.path.join(directory, filename)
        # 读取CSV文件
        data = pd.read_csv(file_path)
        
        # 使用正确的日期列名
        data['date'] = pd.to_datetime(data['date'])
        
        # 裁剪数据，只保留2008年1月1日之后的数据
        filtered_data = data[data['date'] >= pd.Timestamp('2008-01-01')]
        
        # 保存处理后的数据到原文件
        filtered_data.to_csv(file_path, index=False)
        print(f"Processed and saved {filename}")
