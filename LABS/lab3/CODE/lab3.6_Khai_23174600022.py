import pandas as pd

# Đọc tệp stocks1.csv và stocks2.csv vào DataFrame
path_stocks1 = r'C:\Users\Admin\OneDrive\Máy tính\PT NC 2\LABS\lab3\DATA\stocks1.csv'
path_stocks2 = r'C:\Users\Admin\OneDrive\Máy tính\PT NC 2\LABS\lab3\DATA\stocks2.csv'

stocks1 = pd.read_csv(path_stocks1)
stocks2 = pd.read_csv(path_stocks2)

# Gộp hai DataFrame stocks1 và stocks2 thành một DataFrame
chung_khoan = pd.concat([stocks1, stocks2], ignore_index=True)

# Tạo Pivot Table với 'date' làm chỉ mục, 'symbol' làm cột, và giá trị là trung bình của 'close'
pivot_table = pd.pivot_table(chung_khoan, 
                             values='close', 
                             index='date', 
                             columns='symbol', 
                             aggfunc='mean')

# Tính tổng volume giao dịch cho mỗi mã chứng khoán (symbol) và thêm cột mới vào Pivot Table
tong_volume = chung_khoan.groupby('symbol')['volume'].sum()
pivot_table.loc['Tổng volume'] = tong_volume

# Sắp xếp Pivot Table dựa trên tổng volume giao dịch theo thứ tự giảm dần
pivot_table = pivot_table.sort_values(by='Tổng volume', axis=1, ascending=False)

# Hiển thị kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất
print("Kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất:")
print(pivot_table.iloc[:, :5])