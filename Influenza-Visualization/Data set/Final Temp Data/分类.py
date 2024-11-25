import pandas as pd
import os
import shutil

# 设置包含所有气象站CSV文件的文件夹路径
directory = '/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/untitled folder/process data'

# 目标根目录，用于创建state文件夹
root_target_directory = '/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/untitled folder/by_state'

# 确保目标根目录存在
os.makedirs(root_target_directory, exist_ok=True)

# 遍历文件夹中的所有文件
for filename in os.listdir(directory):
    if filename.endswith('.csv'):  # 确保处理的是CSV文件
        file_path = os.path.join(directory, filename)
        
        # 读取CSV文件
        data = pd.read_csv(file_path, encoding='utf-8')
        
        # 检查“state”列并获取其值，假设每个文件只有一个state值
        state = data['State'].iloc[0]
        
        # 创建目标文件夹路径，如果state值为空或异常，使用"Unknown"作为文件夹名
        state_folder = os.path.join(root_target_directory, state if pd.notna(state) else "Unknown")
        
        # 确保目标文件夹存在
        os.makedirs(state_folder, exist_ok=True)
        
        # 定义目标文件路径
        target_file_path = os.path.join(state_folder, filename)
        
        # 移动文件到目标文件夹
        shutil.move(file_path, target_file_path)
        print(f"Moved {filename} to {state_folder}")
