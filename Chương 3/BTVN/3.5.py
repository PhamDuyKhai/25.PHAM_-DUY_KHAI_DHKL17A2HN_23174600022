import numpy as np

# Đọc dữ liệu từ tập tin heights_1.txt và weights_1.txt
with open('heights.txt', 'r') as file:
    height = [float(line.strip()) for line in file]

with open('weights_1.txt', 'r') as file:
    weight = [float(line.strip()) for line in file]

# 1. Tạo numpy array arr_height từ list height.
arr_height = np.array(height)

# 2. Tạo numpy array arr_weight từ list weight.
arr_weight = np.array(weight)

# 3. Cho hệ số quy đổi từ inch sang m là 0.0254, tạo arr_height_m dựa trên công thức: arr_height * hệ số quy đổi.
conversion_factor_height = 0.0254
arr_height_m = arr_height * conversion_factor_height

# 4. Cho hệ số quy đổi từ pound sang kg là 0.453592, tạo arr_weight_kg dựa trên công thức: arr_weight * hệ số quy đổi.
conversion_factor_weight = 0.453592
arr_weight_kg = arr_weight * conversion_factor_weight

# 5. Tính BMI của arr_height_m và arr_weight_kg theo công thức BMI = Cân nặng / (Chiều cao * Chiều cao), và lưu vào arr_bmi.
arr_bmi = arr_weight_kg / (arr_height_m ** 2)

# 6. Cho biết giá trị cân nặng ở vị trí index = 50 trong arr_weight_kg.
weight_at_index_50 = arr_weight_kg[50]
print("Cân nặng ở vị trí index = 50:", weight_at_index_50)

# 7. Tạo arr_height_m_100 gồm các phần tử có vị trí index từ 100 đến 110 (lấy cả index 110) trong arr_height_m.
arr_height_m_100 = arr_height_m[100:111]

# 8. Cho biết các cầu thủ bóng chày có bmi < 21 trong arr_bmi.
bmi_lt_21_indices = np.where(arr_bmi < 21)[0]
print("Cầu thủ có BMI < 21 ở các vị trí:", bmi_lt_21_indices)

# 9. Cho biết chiều cao trung bình và cân nặng trung bình của các cầu thủ.
average_height = np.mean(arr_height_m)
average_weight = np.mean(arr_weight_kg)
print("Chiều cao trung bình:", average_height)
print("Cân nặng trung bình:", average_weight)

# 10. Cho biết chiều cao và cân nặng lớn nhất của các cầu thủ.
max_height = np.max(arr_height_m)
max_weight = np.max(arr_weight_kg)
print("Chiều cao lớn nhất:", max_height)
print("Cân nặng lớn nhất:", max_weight)

# 11. Cho biết chiều cao và cân nặng nhỏ nhất của các cầu thủ.
min_height = np.min(arr_height_m)
min_weight = np.min(arr_weight_kg)
print("Chiều cao nhỏ nhất:", min_height)
print("Cân nặng nhỏ nhất:", min_weight)
