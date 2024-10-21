t = int(input("Nhap thoi gian su dung bong den(h) t:"))
if t > 0:
    U = 220
    I = 2.7
    gia_dien = 7000
    P = t * U * I / 3600 * 1000 
    tien_dien = P * gia_dien
    print(f"Tien dien phai tra la {tien_dien:.2f}")
else:
    print("Khong co gia tri thoa man")
print("Ket thuc chuong trinh")