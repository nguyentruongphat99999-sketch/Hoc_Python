def kiem_tra_email():
    so_lan_sai = 0
    so_lan_nhap_con_lai = 3
    while True:
        email = input("khai bao email:").strip().lower()
        if "@" in email:
            vi_tri_ten = email.find("@")
            ten_nguoi_dung = email[:vi_tri_ten]
            ten_mien = email[vi_tri_ten + 1:]
            if "." in ten_mien:
                print(f"ten mien la:{ten_mien}")
                print(f"ten nguoi dung la:{ten_nguoi_dung}")
                return True
        so_lan_sai = so_lan_sai+1
        so_lan_nhap_con_lai= so_lan_nhap_con_lai-1
        print(f"email ko hop le vui long nhap lai(vui long kiem tra coi co @ va .) ban con {so_lan_nhap_con_lai} lan nhap  \n")
        if so_lan_sai == 3:
            print("tai khoan cua ban da bi khoa")
            return False
print ("=== chuong chinh xac thuc email ===")
ket_qua = kiem_tra_email()
if ket_qua == True:
    print("-> chuc mung ban da dang nhap he thong thanh cong")
else:
    print("-> rat tiet dang nhap that bai do sai qua nhieu lan")
    