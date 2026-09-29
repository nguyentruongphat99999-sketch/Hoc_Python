def kiem_tra_email(email_nhap_vao):
    if "@" in email_nhap_vao:
        vi_tri_ten = email_nhap_vao.find("@")
        ten_mien = email_nhap_vao[vi_tri_ten + 1:]
        if "." in ten_mien:
            return True
    return False
def kiem_tra_mat_khau(mat_khau_nhap_vao):
    return len(mat_khau_nhap_vao) >= 6 
        
danh_sach_email = []
print("=== he thong quan ly danh sach email ===")
print("(nhap 'quanly' de dung nhap 'xoa' de xoa email nhap 'them' de them email")
while True:
    lenh = input("nhap lenh dieu khien:")
    if lenh == "quanly":
        print("-> thanh cong! da thoat che do nhap")
        break
    elif lenh == "them":
        email_nguoi_dung = input("nhap email:").strip().lower()
        mat_khau_nguoi_dung = input("nhap mat khau:").lower()
        is_valid_email = kiem_tra_email(email_nguoi_dung)
        is_valid_mk = kiem_tra_mat_khau(mat_khau_nguoi_dung)
        if is_valid_email and is_valid_mk:
            da_ton_tai = False
            for tk in danh_sach_email:
                if tk["email"] == email_nguoi_dung:
                    da_ton_tai = True
                    break
            if da_ton_tai:
                print("email nay da ton tai trong he thong")
            else:
                tai_khoan_moi ={
                    "email": email_nguoi_dung,
                    "mat_khau": mat_khau_nguoi_dung,
                }
                danh_sach_email.append(tai_khoan_moi)
                print(f"da them tai khoan {email_nguoi_dung} thanh cong!\n")
        elif not is_valid_email and not is_valid_mk:
            print("-> email va mat khau deu khong hop le (email can @ va . , mat khau >= 6)\n")
        elif not is_valid_email:
            print("-> email khong hop le(email can @ va .)\n")
        else:
            print("-> mat khau khong hop le(phai du tu 6 ky tu tro len)\n")
    elif lenh == "xem":
        print("\n---DANH SACH TAI KHOAN CHI TIET---")
        if len(danh_sach_email) ==0:
            print("->danh sach hien dang rong!\n")
        else:
            for stt,tk in enumerate(danh_sach_email,1):
                print (f"{stt}.email:{tk['email']} | mat khau: {tk['mat_khau']}")
            print()
    elif lenh == "xoa":
        email_can_xoa = input("nhap email can xoa:").strip()
        da_xoa = False
        for tk in danh_sach_email:
            if tk["email"]== email_can_xoa:
                danh_sach_email.remove(tk)
                print(f"-> da xoa thanh cong {email_can_xoa}")
                da_xoa = True
                break
        if not da_xoa:
            print(f"khong tim thay{email_can_xoa} trong danh sach")
    else:
        print("-> Lenh khong hop le! Vui long nhap 'them', 'xem', 'xoa' hoac 'quanly'\n")
print("=" * 40)
print(f"Tong so tai khoan dang quan ly: {len(danh_sach_email)}")