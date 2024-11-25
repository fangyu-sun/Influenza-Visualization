# 加载必要的库
library(ggplot2)
library(readr)
library(dplyr)
library(lubridate)

# 读取数据
data <- read_csv("/Users/sunfangyu/Desktop/FIT5147/Assignment DEP/Data set/NNDSS/combined_data.csv")

# 转换日期格式并提取年份和月份
data$Date <- mdy(data$`Week Ending (Friday)`)
data$Year <- year(data$Date)
data$Month <- month(data$Date)

# 筛选出2008年到2022年的数据
filtered_data <- data %>%
  filter(Year >= 2008 & Year <= 2022)

# 计算每个州每月的病例数
monthly_cases <- filtered_data %>%
  group_by(State, Year, Month) %>%
  summarise(Cases = n(), .groups = 'drop')

# 计算每个州每月的平均病例数
average_monthly_cases <- monthly_cases %>%
  group_by(State, Month) %>%
  summarise(Average_Cases = mean(Cases), .groups = 'drop')

# 绘制折线图
ggplot(average_monthly_cases, aes(x = Month, y = Average_Cases, group = State, color = State)) +
  geom_line() +
  scale_x_continuous(breaks = 1:12, labels = month.abb) +
  labs(title = "Average Monthly Influenza Cases by State (2008-2022)",
       x = "Month",
       y = "Average Cases",
       color = "State") +
  theme()

