import os

# 假设您想更改到的目录
new_directory = "/Users/sunfangyu/Desktop/FIT5147/programming exercise 1"

# 更改工作目录
os.chdir(new_directory)

# 验证当前工作目录已经更改
print("当前工作目录：", os.getcwd())
