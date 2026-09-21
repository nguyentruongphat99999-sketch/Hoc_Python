def kiem_tra_email(email_nhap_vao):
    if "@" in email_nhap_vao:
        vi_tri_ten = email_nhap_vao.find("@")
        ten_mien = email_nhap_vao[vi_tri_ten + 1:]
        if "." in ten_mien:
            return True
    return False
danh_sach_email = []
print("=== he thong quan ly danh sach email ===")
print("(nhap 'quanly' bat ky luc nao de xem va dung danh sach)")
while True:
    email_nguoi_dung = input("khai bao email:").strip().lower()
    if email_nguoi_dung == "quanly":
        print("-> thanh cong! da thoat che do nhap")
        break
    if kiem_tra_email(email_nguoi_dung):
        if email_nguoi_dung in danh_sach_email:
            print("email nay da ton tai")
        else:
            danh_sach_email.append(email_nguoi_dung)
            print("-> da them email vao danh sach")
    else:
        print(f"email ko hop le(vui long kiem tra coi co @ va .) \n")
print("=" * 40)
print(f"tong so email da luu: {len(danh_sach_email)}")
print("danh sach chi tiet")
for stt,email in enumerate(danh_sach_email,1):
    print(f"{stt}.{email}")