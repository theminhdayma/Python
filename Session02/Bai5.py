n = input("Nhập một số nguyên dương: ")

if n == n[::-1]:
    print(f"Số {n} là số đối xứng")
else:
    print(f"Số {n} không phải là số đối xứng")
