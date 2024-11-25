import pandas as pd

# 读取流感病例数据
flu_data_path = "/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/NNDSS/processed_data.csv"
flu_data = pd.read_csv(flu_data_path)

# 读取人口数据
population_data_path = "/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/Snapshot of Australia data summary.xlsx"
population_data = pd.read_excel(population_data_path, sheet_name='Table 3')

# 清理人口数据，只保留需要的列
population_data = population_data[['Age group', '2016Persons', '2021Persons']]

# 合并流感数据和人口数据
# 确定使用哪一年的人口数据
flu_data['Population'] = flu_data.apply(lambda row: population_data[population_data['Age group'] == row['Age group']]['2016Persons'].values[0] 
                                        if row['Year'] < 2017 else population_data[population_data['Age group'] == row['Age group']]['2021Persons'].values[0], axis=1)

# 计算发病率：每十万人中的病例数
flu_data['Incidence Rate'] = (flu_data['Total Case Number'] / flu_data['Population']) * 100000

# 保存结果到新的CSV文件
output_file_path = "/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/NNDSS/updated_processed_data.csv"
flu_data.to_csv(output_file_path, index=False)

print(f'Updated data with incidence rate saved to {output_file_path}')
