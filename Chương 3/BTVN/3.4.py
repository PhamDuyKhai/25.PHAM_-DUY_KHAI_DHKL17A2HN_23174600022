import numpy as np

# 1. Tạo arr_zeros có 10 phần tử 0, cập nhật phần tử ở vị trí thứ 5 là 1.
arr_zeros = np.zeros(10)
arr_zeros[4] = 1
print("arr_zeros:", arr_zeros)

# 2. Tạo arr_h có giá trị từ 10 đến 24. In danh sách các phần tử theo tứ tự đảo ngược của arr_h.
arr_h = np.arange(10, 25)
arr_h_reverse = np.flip(arr_h)
print("arr_h_reverse:", arr_h_reverse)

# 3. Cho arr_k và tạo arr_l từ arr_k với các phần tử khác 0.
arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_l = arr_k[arr_k != 0]
print("arr_l:", arr_l)

# 4. Từ arr_l của câu 3, thêm 2 phần tử có giá trị là 10 và 20 vào cuối array.
arr_l = np.append(arr_l, [10, 20])
print("arr_l sau khi thêm 10 và 20:", arr_l)

# 5. Từ array của câu 4, thêm phần tử có giá trị 100 vào vị trí có index = 5.
arr_l = np.insert(arr_l, 5, 100)
print("arr_l sau khi thêm 100 vào index 5:", arr_l)

# 6. Từ array của câu 5, xóa các phần tử tại vị trí có index = 0, 1, 2.
arr_l = np.delete(arr_l, [0, 1, 2])
print("arr_l sau khi xóa các phần tử tại index 0, 1, 2:", arr_l)
