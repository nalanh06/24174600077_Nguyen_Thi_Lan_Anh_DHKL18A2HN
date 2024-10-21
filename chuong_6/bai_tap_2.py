import math
x = float(input("Nhap vao x:"))
if ((x**4 + 1)**(1/7)) != 0:
    f_x = (-x + (x**2 + 4)**(1/2)) / ((x**4 + 1)**(1/7))
    print(f"Gia tri can tim f(x) = {f_x:.2f}")
else:
    print("Khong co gia tri thoa man")
print("Ket thuc chuong trinh")