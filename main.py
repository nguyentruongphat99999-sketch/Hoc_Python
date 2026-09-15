import random
so_bi_mat = random.randint(1, 100)
so_lan_doan = 0
print("=== game doan so bi mat ===")
while True:
    so_lan_doan += 1
    doan = int(input("Nhap so ban doan (1-100): "))
    if doan < 1 or doan > 100:
        print("Vui long nhap so trong khoang 1-100")
        continue
    if doan < so_bi_mat:
        print("so ban doan nho hon so bi mat")
    elif doan > so_bi_mat:
        print("so ban doan lon hon so bi mat")
    else:
        print("Chuc mung! Ban da doan dung so bi mat.")
        break
    
