import pandas as pd
import os

# 设置包含所有气象站CSV文件的文件夹路径
directory = '/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/untitled folder/process data'

# 遍历文件夹中的所有文件
for filename in os.listdir(directory):
    if filename.endswith('.csv'):  # 确保处理的是CSV文件
        file_path = os.path.join(directory, filename)
        
        # 读取CSV文件
        data = pd.read_csv(file_path, encoding='utf-8')
        
        # 检查“site name_y”列是否存在，如果存在则更名为“site name”
        if 'site name_y' in data.columns:
            data.rename(columns={'site name_y': 'site name'}, inplace=True)  # 重命名列
            
            # 保存处理后的数据到原文件
            data.to_csv(file_path, index=False, encoding='utf-8')
            print(f"Renamed 'site name_y' to 'site name' in {filename}")
        else:
            print(f"'site name_y' not found in {filename}")
