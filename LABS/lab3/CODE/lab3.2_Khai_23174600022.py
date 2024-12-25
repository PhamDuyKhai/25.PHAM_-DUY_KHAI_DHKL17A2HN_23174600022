import pandas as pd
file_path = r'C:\Users\Admin\OneDrive\Máy tính\PT NC 2\LABS\lab3\DATA\stocks1.csv'
stocks1 = pd.read_csv(file_path)

#1. Kiểm tra dữ liệu Null trong DataFrame
print(stocks1.isnull().sum())

#2. Tính giá trị trung bình của cột 'high'
mean_high = stocks1['high'].mean()

# Thay thế giá trị Null trong cột 'high'
stocks1['high'].fillna(mean_high, inplace=True)

#3. Tính giá trị trung bình của cột 'low'
mean_low = stocks1['low'].mean()
# Thay thế giá trị Null trong cột 'low'
stocks1['low'].fillna(mean_low, inplace=True)

#4. Xác nhận không còn dữ liệu Null
print(stocks1.info())
