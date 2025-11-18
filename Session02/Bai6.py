N = int(input("Nhập N = "))
factorial = 1
for i in range(1, N + 1):
    factorial *= i
print(f"Giai thừa của {N} là {factorial}")
