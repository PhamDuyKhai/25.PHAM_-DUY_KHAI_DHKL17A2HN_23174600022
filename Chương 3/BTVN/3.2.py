import numpy as np

# 1. Tạo numpy array arr có giá trị từ 0-9 và hiển thị thông tin
arr = np.arange(10)
print("arr:", arr)
print("Kiểu dữ liệu của arr:", arr.dtype)
print("Kích thước của arr:", arr.shape)

# 2. Tạo arr_odd và arr_even từ array arr
arr_odd = arr[arr % 2 != 0]
arr_even = arr[arr % 2 == 0]

print("\narr_odd:", arr_odd)
print("arr_even:", arr_even)

# 3. Tạo arr_update_1 với các phần tử chẵn giữ nguyên, các phần tử lẻ thay bằng 100
arr_update_1 = np.where(arr % 2 == 0, arr, 100)

print("\narr_update_1:", arr_update_1)
