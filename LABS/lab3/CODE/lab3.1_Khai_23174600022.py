import pandas as pd

#1. Đọc file CSV
file_path = r'C:\Users\Admin\OneDrive\Máy tính\PT NC 2\LABS\lab3\DATA\stocks1.csv'
stocks1 = pd.read_csv(file_path)

#2. Hiển thị 5 dòng đầu tiên
print(stocks1.head())

#3. Hiển thị kiểu dữ liệu của mỗi cột
print(stocks1.dtypes)

#4. Xem thông tin tổng quan
print(stocks1.info())

