import pandas as pd

#1. Đọc file csv
stocks1 = pd.read_csv(r'C:\Users\Admin\OneDrive\Máy tính\PT NC 2\LABS\lab3\DATA\stocks1.csv')
stocks2 = pd.read_csv(r'C:\Users\Admin\OneDrive\Máy tính\PT NC 2\LABS\lab3\DATA\stocks2.csv')

# Hiển thị thông tin tổng quan ban đầu của stocks1
print("Thông tin tổng quan ban đầu của stocks1:")
print(stocks1.info())
print("\nKiểu dữ liệu của các cột trong stocks1:")
print(stocks1.dtypes)

# Kiểm tra dữ liệu Null và xử lý dữ liệu thiếu trong stocks1
print("\nKiểm tra dữ liệu Null trong stocks1:")
print(stocks1.isnull().sum())
stocks1['high'].fillna(stocks1['high'].mean(), inplace=True)
stocks1['low'].fillna(stocks1['low'].mean(), inplace=True)
print("\nKiểm tra lại dữ liệu Null sau khi xử lý:")
print(stocks1.isnull().sum())

#2. Gộp hai DataFrame stocks1 và stocks2
stocks = pd.concat([stocks1, stocks2], ignore_index=True)
print("\nDataFrame sau khi gộp stocks1 và stocks2:")
print(stocks.head())
print("\nThông tin tổng quan của DataFrame stocks sau khi gộp:")
print(stocks.info())

#3. Tính giá trung bình (open, high, low, close) cho mỗi ngày
gia_tb_moi_ngay = stocks.groupby('date')[['open', 'high', 'low', 'close']].mean()
print("\nGiá trị trung bình (open, high, low, close) cho mỗi ngày:")
print(gia_tb_moi_ngay.head())

#4. Hiển thị 5 dòng đầu tiên
print('\nDữ liệu 5 dòng đầu:\n',stocks.head())
