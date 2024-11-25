import pandas as pd
import os

# 站点描述文件路径
site_data_path = '/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/112 site data/Book1.csv'

# 读取站点描述文件，确保使用utf-8编码
site_data = pd.read_csv(site_data_path, encoding='utf-8')

# 设置包含所有气象站CSV文件的文件夹路径
directory = '/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/untitled folder/process data'

# 遍历文件夹中的所有文件
for filename in os.listdir(directory):
    if filename.endswith('.csv'):  # 确保处理的是CSV文件
        file_path = os.path.join(directory, filename)
        
        # 读取每个站点的CSV文件，确保使用utf-8编码
        temp_data = pd.read_csv(file_path, encoding='utf-8')
        
        # 检查是否已经存在站点相关的列，如果不存在，则进行合并
        if not {'site name', 'longitude', 'latitude', 'locality', 'state'}.issubset(temp_data.columns):
            # 根据site number将站点描述信息合并到温度数据中
            merged_data = pd.merge(temp_data, site_data, on='site number', how='left')
            # 保存处理后的数据到原文件，确保使用utf-8编码
            merged_data.to_csv(file_path, index=False, encoding='utf-8')
            print(f"Updated site data added to {filename}")
        else:
            print(f"Site data already exists in {filename}, no update made.")
