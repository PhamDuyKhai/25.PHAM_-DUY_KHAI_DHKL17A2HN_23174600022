import pandas as pd

# Đọc tệp stocks1.csv và stocks2.csv vào DataFrame
path_stocks1 = r'C:\Users\Admin\OneDrive\Máy tính\PT NC 2\LABS\lab3\DATA\stocks1.csv'
path_stocks2 = r'C:\Users\Admin\OneDrive\Máy tính\PT NC 2\LABS\lab3\DATA\stocks2.csv'

stocks1 = pd.read_csv(path_stocks1)
stocks2 = pd.read_csv(path_stocks2)

# Gộp hai DataFrame stocks1 và stocks2 thành một DataFrame
chung_khoan = pd.concat([stocks1, stocks2], ignore_index=True)

# Tạo MultiIndex cho DataFrame bằng cách sử dụng cột 'date' và 'symbol' làm chỉ mục
chung_khoan = chung_khoan.set_index(['date', 'symbol'])

# Sử dụng GroupBy để tính giá trị trung bình của các cột (open, high, low, close) và volume cho mỗi ngày, mỗi mã chứng khoán
tb_theo_chi_muc = chung_khoan.groupby(['date', 'symbol']).mean()

# Sắp xếp dữ liệu theo ngày và mã chứng khoán
tb_theo_chi_muc = tb_theo_chi_muc.sort_index()

# Hiển thị kết quả cho 5 ngày đầu tiên
print("Kết quả dữ liệu trung bình (open, high, low, close, volume) cho 5 ngày đầu tiên:")
print(tb_theo_chi_muc.head())