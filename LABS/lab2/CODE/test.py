import csv
import numpy as np

# 1. Đọc file CSV và lưu dữ liệu vào một list
file_path = r'C:\Users\Admin\OneDrive\Máy tính\PT NC 2\LABS\lab2\DATA\diem_hoc_phan.csv'
data = []

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Bỏ qua hàng đầu tiên (tiêu đề cột)
    
    # Xử lý dữ liệu từ mỗi hàng
    for row in reader:
        # Chuyển đổi điểm số từ string sang float và thêm vào list
        data.append([float(score) for score in row[2:]])

# Hiển thị một phần của dữ liệu để kiểm tra
print(data[:5])  # Hiển thị 5 dòng đầu tiên

# 2. Chuyển đổi điểm số sang hệ chữ
def chuyen_diem(score):
    """Chuyển đổi điểm số sang điểm chữ theo tiêu chí đã cho."""
    if 8.5 <= score <= 10:
        return 'A'
    elif 8.0 <= score < 8.5:
        return 'B+'
    elif 7.0 <= score < 8.0:
        return 'B'
    elif 6.5 <= score < 7.0:
        return 'C+'
    elif 5.5 <= score < 6.5:
        return 'C'
    elif 5.0 <= score < 5.5:
        return 'D+'
    elif 4.0 <= score < 5.0:
        return 'D'
    else:
        return 'F'

# Áp dụng hàm quy đổi cho mỗi điểm
diem_np_array = np.array(data)
diem_converted = np.vectorize(chuyen_diem)(diem_np_array)

# Hiển thị 5 dòng đầu tiên của mảng điểm chữ
print(diem_converted[:5])

# 3. Phân tích dữ liệu điểm số
# Chia tách dữ liệu để phân tích điểm số của mỗi học phần
hp1_scores = diem_np_array[:, 0]  # Điểm học phần 1
hp2_scores = diem_np_array[:, 1]  # Điểm học phần 2
hp3_scores = diem_np_array[:, 2]  # Điểm học phần 3

# Tính toán thống kê cơ bản
hp1_stats = (np.sum(hp1_scores), np.mean(hp1_scores), np.std(hp1_scores))
hp2_stats = (np.sum(hp2_scores), np.mean(hp2_scores), np.std(hp2_scores))
hp3_stats = (np.sum(hp3_scores), np.mean(hp3_scores), np.std(hp3_scores))

# Báo cáo kết quả ra màn hình
print("Học Phần 1:")
print(f"Tổng điểm: {hp1_stats[0]:.2f}")
print(f"Điểm trung bình: {hp1_stats[1]:.2f}")
print(f"Độ lệch chuẩn: {hp1_stats[2]:.2f}\n")

print("Học Phần 2:")
print(f"Tổng điểm: {hp2_stats[0]:.2f}")
print(f"Điểm trung bình: {hp2_stats[1]:.2f}")
print(f"Độ lệch chuẩn: {hp2_stats[2]:.2f}\n")

print("Học Phần 3:")
print(f"Tổng điểm: {hp3_stats[0]:.2f}")
print(f"Điểm trung bình: {hp3_stats[1]:.2f}")
print(f"Độ lệch chuẩn: {hp3_stats[2]:.2f}\n")

# 4. Phân tích tổng quan cho toàn bộ lớp học
tong_diem_all = np.sum(diem_np_array)
diem_tb_all = np.mean(diem_np_array)
std_deviation_all = np.std(diem_np_array)

print("Tổng quan toàn bộ lớp học:")
print(f"Tổng điểm của toàn lớp (cho tất cả học phần): {tong_diem_all:.2f}")
print(f"Điểm trung bình của toàn lớp (cho tất cả học phần): {diem_tb_all:.2f}")
print(f"Độ lệch chuẩn của toàn lớp: {std_deviation_all:.2f}")
