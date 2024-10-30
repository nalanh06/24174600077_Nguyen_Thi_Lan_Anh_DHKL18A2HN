#Câu 8
diem_chuyen_can = float(input("Nhap diem chuyen can:"))
diem_giua_ky = float(input("Nhap diem giua ky:"))
diem_cuoi_ky = float(input("Nhap diem cuoi ky:"))
diem_trung_binh = (diem_chuyen_can + diem_giua_ky + diem_cuoi_ky) / 3
if diem_trung_binh >= 9:
    print("Loai A")
elif diem_trung_binh >= 7:
    print("Loai B")
elif diem_trung_binh >= 5:
    print("Loai C")
else:
    print("Loai D")
print(f"Diem trung binh la:{diem_trung_binh}")