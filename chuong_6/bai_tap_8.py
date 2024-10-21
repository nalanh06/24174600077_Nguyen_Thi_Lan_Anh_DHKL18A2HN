import math
x = input("Nhap gia tri x")
if x > 0:
    x = float(x)
    f_x = math.log(x, 4) + math.log(2, x)
    print(f"Gia tri can tim f(x) = {f_x:.2f}")
else:
    print("Khong co gia tri thoa man")
print("Ket thuc chuong trinh")