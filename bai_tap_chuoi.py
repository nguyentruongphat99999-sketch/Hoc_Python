email = input("khai bao email:").strip().lower()
if "@" in email:
    vi_tri_ten = email.find("@")
    ten_nguoi_dung = email[:vi_tri_ten]
    ten_mien = email[vi_tri_ten + 1:]
    print(f"ten nguoi dung la:{ten_nguoi_dung}")
    print(f"ten mien la:{ten_mien}")
else:
    print(f"day khong email hop le(vi ko co dau @)")
