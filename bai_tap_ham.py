def kiem_tra_email(email_nhap_vao):
    if "@" in email_nhap_vao:
        vi_tri_ten = email_nhap_vao.find("@")
        ten_mien = email_nhap_vao[vi_tri_ten + 1:]
        if "." in ten_mien:
            return True
    return False
so_lan_sai=0
so_lan_nhap_con_lai=3
while True:
    email_nguoi_dung = input("khai bao email:").strip().lower()
    is_valid = kiem_tra_email(email_nguoi_dung)
    if is_valid == True:
        print ("ban da dang nhap thanh cong")
        break
    so_lan_sai = so_lan_sai+1
    so_lan_nhap_con_lai= so_lan_nhap_con_lai-1
    if so_lan_sai==3:
        print("tai khoan cua ban da bi khoa")
        break
    print(f"email ko hop le vui long nhap lai(vui long kiem tra coi co @ va .) ban con {so_lan_nhap_con_lai} lan nhap  \n")
