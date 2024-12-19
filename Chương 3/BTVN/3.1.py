import numpy as np

# Lấy và hiển thị phiên bản NumPy
numpy_version = np.__version__
print("Phiên bản NumPy hiện tại:", numpy_version)

# Hiển thị cấu hình xây dựng của NumPy
numpy_build_config = np.show_config()
print("\nCấu hình xây dựng của NumPy:")
print(numpy_build_config)
