
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(1000)

# Thiết lập phong cách hiển thị
sns.set_theme(style="whitegrid")

# Tạo ra 1 dữ liệu 
tips = sns.load_dataset("tips")

# Tạo figure thông qua plt
plt.figure(figsize=(10, 6))

# hisplot
sns.histplot(
    tips,
    bins=30,
    color="skyblue",
)

# Đặt tiêu đề và nhãn cho biểu đồ
plt.title("Tiêu đề biểu đồ", fontsize=16)
plt.xlabel("Trục X", fontsize=14)
plt.ylabel("Trục Y", fontsize=14)

# Hiển thị biểu đồ
plt.show()
