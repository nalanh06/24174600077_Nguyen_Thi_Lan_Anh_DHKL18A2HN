r = float(input("Nhap vao ban kinh r:"))
h = float(input("Nhap vao chieu cao h:"))
if h > 0 and r > 0:
    pi = 3.14
    dien_tich_xung_quanh_hinh_tru = 2 * pi * r * h
    dien_tich_toan_phan_hinh_tru = 2 * pi * r ** 2 + 2 * pi * r * h
    the_tich = pi * r ** 2
    print(f"dien tich xung quanh hinh tru la {dien_tich_xung_quanh_hinh_tru:.2f}")
    print(f"dien tich toan phan hinh tru la {dien_tich_toan_phan_hinh_tru:.2f}")
    print(f"the tich hinh tru la {the_tich:.2f}")
else:
    print("Gia tri nhap khong thoa man")
print("Ket thuc chuong trinh")