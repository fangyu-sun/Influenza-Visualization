import json

# 指定JSON文件的路径
json_file_path = '/Users/sunfangyu/Desktop/FIT5147/DVP/JS/Map/combined_all_states_temp.json'

# 读取JSON文件
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# 检查数据条数
num_records = len(data)

# 打印数据条数
print(f'The JSON file contains {num_records} records.')
