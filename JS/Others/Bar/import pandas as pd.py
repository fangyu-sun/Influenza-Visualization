import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('/Users/sunfangyu/Desktop/FIT5147/DVP/JS/combined_flu_data.csv', dtype={'Age group': str})

# 将 "Age group" 列中的 "-" 转换成 "~"
df['Age group'] = df['Age group'].str.replace('-', '~')

# 恢复被错误识别为日期格式的内容
df['Age group'] = df['Age group'].replace({'5~Sep': '05~09', 'Oct~14': '10~14'})

# 确保数据处理正确
print(df)

# 保存为新的 CSV 文件
df.to_csv('/Users/sunfangyu/Desktop/FIT5147/DVP/JS/processed_combined_flu_data.csv', index=False)
