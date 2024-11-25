import pandas as pd
import os

# 定义根目录路径，其中包含所有州的文件夹
root_directory = '/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/untitled folder/by_state'

# 遍历每个州的文件夹
for state_folder in os.listdir(root_directory):
    state_path = os.path.join(root_directory, state_folder)
    if os.path.isdir(state_path):
        state_data = pd.DataFrame()
        
        # 读取该州文件夹中的所有CSV文件
        for file in os.listdir(state_path):
            if file.endswith('.csv'):
                file_path = os.path.join(state_path, file)
                temp_data = pd.read_csv(file_path)
                temp_data['date'] = pd.to_datetime(temp_data['date'])  # 格式化日期
                temp_data['mean temperature (degC)'] = pd.to_numeric(temp_data['mean temperature (degC)'], errors='coerce')  # 转换为数值
                
                state_data = pd.concat([state_data, temp_data], ignore_index=True)
        
        # 计算每天的平均温度
        daily_avg_temp = state_data.groupby('date')['mean temperature (degC)'].mean().reset_index()
        
        # 定义输出文件的名称和路径
        output_filename = f"{state_folder}_meantemp.csv"
        output_path = os.path.join(state_path, output_filename)
        
        # 保存计算结果到CSV文件
        daily_avg_temp.to_csv(output_path, index=False)
        print(f"Daily average temperature calculated and saved for {state_folder} in {output_filename}")
