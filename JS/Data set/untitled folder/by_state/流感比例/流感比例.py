import pandas as pd

# 读取CSV文件
file_path = "/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/NNDSS/combined_data.csv"
data = pd.read_csv(file_path)

# 确定日期列的正确格式并将其转换为日期类型，这里使用 dayfirst=True 来正确解析日在前的格式
data['Year'] = pd.to_datetime(data['Week Ending (Friday)'], dayfirst=True).dt.year

# 按照年份和年龄组分组，然后计算每组的病例总数
grouped_data = data.groupby(['Year', 'Age  group']).size().reset_index(name='Total Case Number')

# 保存新的CSV文件
output_file_path = "/Users/sunfangyu/Desktop/processed_data.csv"
grouped_data.to_csv(output_file_path, index=False)

print(f'Processed data saved to {output_file_path}')
