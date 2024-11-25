import csv
import requests
from bs4 import BeautifulSoup

# 输入和输出文件的路径
input_csv_path = (
    "/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/ACORN-SAT/station_urls.csv"
)
output_csv_path = (
    "/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/ACORN-SAT/station_details.csv"
)

# 读取URLs
with open(input_csv_path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # 跳过标题行
    urls = [row[0] for row in reader]

# 准备收集站点信息的列表
stations_info = []

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    #    print(stations_info)
    print(soup)
#     # 根据实际HTML结构提取所需信息
#     # 以下选择器是假设的，需要根据实际情况调整
#     site_name = soup.find("span", id="site_name").text
#     site_number = soup.find("span", id="stn_num").text
#     latitude = soup.find("span", id="latitude").text
#     longitude = soup.find("span", id="longitude").text
#     elevation = soup.find("span", id="elevation").text
#     locality = soup.find("span", id="locality").text.split(", ")
#     locality_city = locality[0]
#     locality_state = locality[1] if len(locality) > 1 else ""

#     print(soup.prettify())
# #     # 将提取的信息添加到列表
# #     stations_info.append(
# #         [
# #             site_name,
# #             site_number,
# #             latitude,
# #             longitude,
# #             elevation,
# #             locality_city,
# #             locality_state,
# #         ]
# #     )

# # # 写入新的CSV文件
# # with open("station_information.csv", "a", newline="", encoding="utf-8") as file:
# #     writer = csv.writer(file)
# #     # 只有在写入第一个站点信息时才写入标题头
# #     # writer.writerow(['Site name', 'Site number', 'Latitude', 'Longitude', 'Elevation', 'Locality city', 'Locality state'])
# #     writer.writerow(
# #         [
# #             site_name,
# #             site_number,
# #             latitude,
# #             longitude,
# #             elevation,
# #             locality_city,
# #             locality_state,
# #         ]
# #     )

# # print("站点信息已保存到CSV文件。")
