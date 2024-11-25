import os
import pandas as pd

# 设置文件夹路径
folder_path = '/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/acorn_sat_v2.4.0_daily_tmean'

# 初始化缺失数据统计字典和总缺失量计数器
missing_data_summary = {}
total_missing_count = 0
files_with_missing_temp = 0

# 遍历文件夹中的所有CSV文件
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        # 读取CSV文件
        data = pd.read_csv(file_path)
        # 过滤2008年以后的数据
        data['date'] = pd.to_datetime(data['date'])
        data = data[data['date'].dt.year >= 2008]
        # 忽略'site number'和'site name'列
        data = data.drop(columns=['site number', 'site name'], errors='ignore')
        # 检查每列的缺失值
        missing_count_per_column = data.isnull().sum()
        
        # 获取'mean temperature (degC)'的缺失数量
        missing_temp_count = missing_count_per_column.get('mean temperature (degC)', 0)
        # 更新总缺失数量
        total_missing_count += missing_temp_count
        
        # 记录有缺失的文件和具体缺失信息
        if missing_temp_count > 0:
            files_with_missing_temp += 1
            missing_data_summary[filename] = {'mean temperature (degC)': missing_temp_count}

# 输出缺失数据的详细信息
for file, details in missing_data_summary.items():
    print(f"File: {file}")
    for column, count in details.items():
        print(f"  Missing in column: {column}, Count: {count}")
    print()  # 空行，用于分隔文件的输出

# 输出总缺失量和受影响的文件数量
print(f"Total files with missing 'mean temperature (degC)' data: {files_with_missing_temp}")
print(f"Total missing 'mean temperature (degC)' data entries: {total_missing_count}")
