email = input("khai bao email:")
vi_tri_ten = email.find("@")
ten_nguoi_dung = email[:vi_tri_ten]
ten_mien = email[vi_tri_ten + 1:]
print("ten nguoi dung la:",ten_nguoi_dung)
print("ten mien la:",ten_mien)