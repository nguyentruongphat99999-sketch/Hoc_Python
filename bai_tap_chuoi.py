email = input("khai bao email:").strip().lower()
if "@" in email:
    vi_tri_ten = email.find("@")
    ten_nguoi_dung = email[:vi_tri_ten]
    ten_mien = email[vi_tri_ten + 1:]
    if "." in ten_mien:
        print(f"ten mien la:{ten_mien}")
        print(f"ten nguoi dung la:{ten_nguoi_dung}")
    else:
        print("ten mien ko hop le(vi thieu dau .)")
else:
    print(f"day khong email hop le(vi ko co dau @)")
