import pandas as pd
import os

# 文件夹路径，包含所有要合并的CSV文件
directory = '/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/untitled folder/by_state/111State mean Temp'

# 初始化空的DataFrame
combined_df = pd.DataFrame()

# 遍历文件夹中的所有CSV文件
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        # 读取CSV文件
        temp_df = pd.read_csv(file_path)
        # 将读取的数据追加到combined_df中
        combined_df = pd.concat([combined_df, temp_df], ignore_index=True)

# 定义输出文件路径
output_path = os.path.join(directory, 'combined_all_states.csv')

# 保存合并后的DataFrame到CSV文件
combined_df.to_csv(output_path, index=False)
print(f"Combined CSV file saved to {output_path}")
