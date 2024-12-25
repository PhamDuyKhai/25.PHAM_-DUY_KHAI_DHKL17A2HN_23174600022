import pandas as pd

# Đọc tệp companies.csv vào DataFrame
path_companies = r'C:\Users\Admin\OneDrive\Máy tính\PT NC 2\LABS\lab3\DATA\companies.csv'
cong_ty = pd.read_csv(path_companies)

# Hiển thị 5 dòng đầu tiên của DataFrame công ty
print("5 dòng đầu tiên của DataFrame công ty:")
print(cong_ty.head())

# Đọc tệp stocks1.csv và stocks2.csv vào DataFrame
path_stocks1 = r'C:\Users\Admin\OneDrive\Máy tính\PT NC 2\LABS\lab3\DATA\stocks1.csv'
path_stocks2 = r'C:\Users\Admin\OneDrive\Máy tính\PT NC 2\LABS\lab3\DATA\stocks2.csv'

stocks1 = pd.read_csv(path_stocks1)
stocks2 = pd.read_csv(path_stocks2)

# Gộp hai DataFrame stocks1 và stocks2 thành một DataFrame

# Kiểm tra dữ liệu Null và xử lý dữ liệu thiếu trong stocks1
print("\nKiểm tra dữ liệu Null trong stocks1:")
print(stocks1.isnull().sum())
stocks1['high'].fillna(stocks1['high'].mean(), inplace=True)
stocks1['low'].fillna(stocks1['low'].mean(), inplace=True)
print("\nKiểm tra lại dữ liệu Null sau khi xử lý:")
print(stocks1.isnull().sum())


#2. Gộp hai DataFrame stocks1 và stocks2

#đổi tên cột name ở file company(vì ko kốc cột symbol ở cột company )
cong_ty.rename(columns={'name': 'symbol'}, inplace=True)

stocks = pd.concat([stocks1, stocks2], ignore_index=True)
print("\nDataFrame sau khi gộp stocks1 và stocks2:")
print(stocks.head())
print("\nThông tin tổng quan của DataFrame stocks sau khi gộp:")
print(stocks.info())
chung_khoan = pd.concat([stocks1, stocks2], ignore_index=True)

# Kết hợp DataFrame chứng khoán với DataFrame công ty dựa trên cột 'symbol'
gop = pd.merge(chung_khoan, cong_ty, on='symbol')

# Tính giá đóng cửa trung bình cho mỗi công ty
dong_cua_tb_theo_cong_ty = gop.groupby('symbol')['close'].mean()

# Hiển thị kết quả cho 5 công ty đầu tiên
print("\nGiá đóng cửa trung bình của 5 công ty đầu tiên:")
print(dong_cua_tb_theo_cong_ty.head())