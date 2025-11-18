a = int(input("Nhập số nguyên a = "))
b = int(input("Nhập số nguyên b = "))
print(f"Các số nguyên tố từ {a} đến {b} là: ")
for num in range(a, b + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)
