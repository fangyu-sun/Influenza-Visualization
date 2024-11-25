import pandas as pd
import os
import re

# 设置包含所有气象站CSV文件的文件夹路径
directory = '/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/untitled folder/process data'

# 遍历文件夹中的所有文件
for filename in os.listdir(directory):
    if filename.endswith('.csv'):  # 确保处理的是CSV文件
        file_path = os.path.join(directory, filename)
        
        # 使用正则表达式从文件名中提取站点编号
        site_number = re.search(r'\d+', filename).group()
        
        # 读取CSV文件
        data = pd.read_csv(file_path)
        
        # 检查是否存在'site number'列，如果不存在则创建
        if 'site number' not in data.columns:
            data['site number'] = None
        
        # 将站点编号赋值给'site number'列
        data['site number'] = site_number
        
        # 保存处理后的数据到原文件
        data.to_csv(file_path, index=False)
        print(f"Processed and added site number to {filename}")
