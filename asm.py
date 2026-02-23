def lt():
    LT01="Laptop Gaming Acer Nitro 5"
    LT02="Laptop Asus TUF FX506"
    LT03="Laptop Dell Inspiron 15"
    LT04="Laptop HP Pavilion 14"
    th1="Acer"
    th2="Asus"
    th3="Dell"
    th4="HP"
    gia1=20000000
    gia2=18500000
    gia3=16000000
    gia4=17000000
    ton_kho1=8
    ton_kho2=11
    ton_kho3=9
    ton_kho4=15
    while True:
        print("----MENU---")
        print("1. Danh sách sản phẩm")
        print("2. Thêm sản phẩm")
        print("0. Thoát")
        a=int(input("Nhập lựa chọn:"))
        if a==1:
            while True:
                print("------Danh sách sản phẩm------")
                print("| LT01: Laptop Gaming Acer Nitro 5")
                print("| LT02: Laptop Asus TUF FX506")
                print("| LT03: Laptop Dell Inspiron 15")
                print("| LT04: Laptop HP Pavilion 14")
                print("--------------------")
                print("Nhập 0 để thoát.")
                ltp=input("Nhập mã sản phẩm:").lower()
                if ltp=="lt01":
                    print("----------")
                    print("Tên sản phẩm:",LT01,)
                    print("Thương hiệu:",th1)
                    print("Giá:",gia1,"VND")
                    print("Số lượng tồn kho:",ton_kho1)
                    print("----------")
                    print("Nhập 0 để thoát.")
                elif ltp=="lt02":
                    print("----------")
                    print("Tên sản phẩm:",LT02)
                    print("Thương hiệu:",th2)
                    print("Giá:",gia2,"VND")
                    print("Số lượng tồn kho:",ton_kho2)
                    print("----------")
                    print("Nhập 0 để thoát.")
                elif ltp=="lt03":
                    print("----------")
                    print("Tên sản phẩm:",LT03)
                    print("Thương hiệu:",th3)
                    print("Giá:",gia3,"VND")
                    print("Số lượng tồn kho:",ton_kho3)
                    print("----------")
                    print("Nhập 0 để thoát.")
                elif ltp=="lt04":
                    print("----------")
                    print("Tên sản phẩm:",LT04)
                    print("Thương hiệu:",th4)
                    print("Giá:",gia4,"VND")
                    print("Số lượng tồn kho:",ton_kho4)
                    print("----------")
                    print("Nhập 0 để thoát.")
                elif ltp=="0":
                    print("Thoát")
                    break
                else:
                    print("Mã sản phẩm không tồn tại")
                    print("----------")
        elif a==0:
            print("Thoát Menu. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại")
lt()


