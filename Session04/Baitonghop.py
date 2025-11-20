products = []


def add():
    product_id = input("Nhập mã sản phẩm: ")

    for product in products:
        if product['Mã sản phẩm'] == product_id:
            print("Mã sản phẩm đã tồn tại. Vui lòng nhập mã khác.")
            return

    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))
    quantity = int(input("Nhập số lượng sản phẩm: "))
    products.append((product_id, name, price, quantity))
    print("Đã thêm sản phẩm thành công.")


def display():
    if not products:
        print("Danh sách sản phẩm trống.")
        return
    print("Danh sách sản phẩm:")
    for product in products:
        print(
            f"Mã sản phẩm: {product[0]}, "
            f"Tên sản phẩm: {product[1]}, "
            f"Giá: {product[2]}, "
            f"Số lượng: {product[3]}"
        )


def search():
    product_id = input("Nhập mã sản phẩm cần tìm: ")
    for product in products:
        if product[0] == product_id:
            print(
                f"Tìm thấy sản phẩm: "
                f"Mã sản phẩm: {product[0]}, "
                f"Tên sản phẩm: {product[1]}, "
                f"Giá: {product[2]}, "
                f"Số lượng: {product[3]}"
            )
            return
    print("Không tìm thấy sản phẩm với mã đã nhập.")


def update():
    product_id = input("Nhập mã sản phẩm cần cập nhật: ")

    for product in products:
        if product[0] == product_id:
            name = input("Nhập tên sản phẩm mới: ")
            price = float(input("Nhập giá sản phẩm mới: "))
            quantity = int(input("Nhập số lượng sản phẩm mới: "))

            index = products.index(product)
            products[index] = (product_id, name, price, quantity)

            print("Đã cập nhật thông tin sản phẩm thành công.")
            return

    print("Không tìm thấy sản phẩm với mã đã nhập.")


def delete():
    product_id = input("Nhập mã sản phẩm cần xóa: ")

    for product in products:
        if product[0] == product_id:
            products.remove(product)
            print("Đã xóa sản phẩm thành công.")
            return

    print("Không tìm thấy sản phẩm với mã đã nhập.")


while True:
    print("**************MENU****************")
    print("1. Thêm sản phẩm mới")
    print("2. Hiển thị danh sách sản phẩm")
    print("3. Tìm kiếm sản phẩm theo mã sản phẩm")
    print("4. Cập nhật thông tin sản phẩm")
    print("5. Xóa sản phẩm theo mã sản phẩm")
    print("0. Thoát chương trình")

    choice = input("Nhập từ 1 đến 5 để chọn chức năng, hoặc 0 để thoát: ")

    if choice == '1':
        add()
    elif choice == '2':
        display()
    elif choice == '3':
        search()
    elif choice == '4':
        update()
    elif choice == '5':
        delete()
    elif choice == '0':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
