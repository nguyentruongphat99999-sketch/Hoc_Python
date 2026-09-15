danh_sach_chi_tieu = []
while True :
    print("\n=== Quan ly chi tieu ===")
    print("1. them khoan chi")
    print("2. xem danh sach chi tieu")
    print("3. tinh tong tien da chi ")
    print("4. thoat")
    lua_chon = input("Nhap lua chon cua ban:(1-4) ")
    if lua_chon == "1":
        ten = input("nhap ten khoan chi:")
        tien = float(input("nhap so tien da chi:"))
        danh_sach_chi_tieu.append((ten, tien))
    elif lua_chon == "2":
        print("\n === danh sach chi tieu ===")
        for i, (ten, tien) in enumerate(danh_sach_chi_tieu, start=1):
            print(f"{i}. {ten}: {tien} VND")
    elif lua_chon == "3":
        tong_tien = sum(tien for _, tien in danh_sach_chi_tieu)
        print(f"\nTong tien da chi: {tong_tien} VND")
    elif lua_chon == "4":
        print("Thoat chuong trinh.")
        break