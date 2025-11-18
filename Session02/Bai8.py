# Nhập vào 3 số nguyên và kiểm tra có phải là hình tam giác không
a = int(input("Nhập số nguyên a = "))
b = int(input("Nhập số nguyên b = "))
c = int(input("Nhập số nguyên c = "))

if a + b > c and a + c > b and b + c > a:
    print("Là 3 cạnh của một tam giác")
else:
    print("Không phải là 3 cạnh của một tam giác")
