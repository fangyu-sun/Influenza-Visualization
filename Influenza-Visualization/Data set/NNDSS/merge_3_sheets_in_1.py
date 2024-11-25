import pandas as pd

# 设置Excel文件的路径
file_path = '/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/NNDSS copy/national-notifiable-diseases-surveillance-system-nndss-public-dataset-influenza-laboratory-confirmed.xlsx'

# 读取Excel文件的所有sheets
xls = pd.ExcelFile(file_path)
sheets = xls.sheet_names  # 获取所有sheet的名称

# 初始化一个空的DataFrame列表
dfs = []

# 对每个sheet进行处理
for sheet in sheets:
    df = pd.read_excel(file_path, sheet_name=sheet, parse_dates=False)
    # 转换 'Age  group' 列为字符串
    df['Age  group'] = df['Age  group'].astype(str)
    # 替换错误的日期格式
    df['Age  group'] = df['Age  group'].replace({
        '5-Sep': '05-09',
        'Oct-14': '10-14'
    }, regex=True)
    dfs.append(df)

# 合并所有DataFrame，ignore_index=True保证合并后的索引是连续的
combined_df = pd.concat(dfs, ignore_index=True)

# 将合并后的DataFrame保存为CSV文件
combined_df.to_csv('/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/NNDSS copy/combined_data.csv', index=False)
