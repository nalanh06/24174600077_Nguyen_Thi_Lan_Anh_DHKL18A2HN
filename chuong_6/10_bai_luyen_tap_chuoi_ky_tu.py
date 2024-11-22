# Bài 1: Viết chương trình nhập vào chuỗi ký tự, trả về số các từ trong chuỗi ký tự vừa nhập
# Ví dụ: Nhập vào: “Hom nay    troi   mua   ”          Trả về: 4
chuoi_nhap_vao = input("Nhap vao chuoi bat ki: ")
chuoi_da_xoa_khoang_trong_dau_cuoi = chuoi_nhap_vao.strip()
chuoi_da_xoa_khoang_trong = chuoi_da_xoa_khoang_trong_dau_cuoi.split()
so_cac_tu = len(chuoi_da_xoa_khoang_trong)
print(f"So cac tu trong chuoi la: {so_cac_tu}")

# Bài 2: Viết chương trình nhập vào chuỗi ký tự, trả về chuỗi ký tự sau khi loại bỏ tất cả các dấu cách thừa
# Ví dụ: Nhập vào: “Hom nay    troi   mua   ”
#              Trả về: “Hom nay troi mua”
chuoi_nhap_vao = input("Nhap vao chuoi bat ki: ")
tach_chuoi = chuoi_nhap_vao.split()
chuoi_ket_qua = " ".join(tach_chuoi)
print(f"Chuoi ket qua la: {chuoi_ket_qua}")

# Bài 3: Viết chương trình nhập vào họ tên đầy đủ, trả về tên và họ riêng
# Ví dụ: Nhập vào: “Vo Van Nam”
#              Trả về: “Ho: Vo, Ten: Nam”
ho_va_ten = input("Nhap ho va ten: ")
tach_chuoi = ho_va_ten.split()
ho = tach_chuoi[0]
ten = tach_chuoi[-1]
print(f"Ho: {ho}, Ten: {ten}")

# Bài 4: Viết chương trình nhập vào chuỗi ký tự, trả về kết quả đếm số ký tự là chữ, số ký tự là số và số ký tự là ký tự đặc biệt (Không là số, không là chữ) trong chuỗi
chuoi_nhap_vao = input("Nhap vao chuoi bat ki: ")
dem_chu = 0
dem_so = 0
dem_ky_tu_dac_biet = 0
for chu in chuoi_nhap_vao:
    if chu.isalpha() == True:
        dem_chu += 1
    else:
        if chu.isdigit() == True:
            dem_so += 1
        else:
            dem_ky_tu_dac_biet += 1
print(f"So chu cai: {dem_chu}")
print(f"So so: {dem_so}")
print(f"So ky tu dac biet: {dem_ky_tu_dac_biet}")

# Bài 5: Viết chương trình nhập vào chuỗi ký tự, đếm xem có bao nhiêu chữ cái viết hoa, bao nhiêu chữ cái viết thường
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
dem_chu_hoa = 0
dem_chu_thuong = 0
for chu in chuoi_nhap_vao:
    if chu.isupper() == True:
        dem_chu_hoa += 1
    else:
        if chu.islower() == True:
            dem_chu_thuong += 1
print(f"So chu viet hoa: {dem_chu_hoa}")
print(f"So chu viet thuong: {dem_chu_thuong}")

# Bài 6:  Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải là số âm hay không
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
chuoi_da_xoa_khoang_trong = chuoi_nhap_vao.replace(" ", "")
if chuoi_da_xoa_khoang_trong[1:-1].isdigit():
    if chuoi_da_xoa_khoang_trong[0]=="-":
        print("La chuoi so am")
    else:
        print("Khong la chuoi so am")
else:
    print("Khong phai chuoi so")

# Bài 8: Viết chương trình nhập vào 2 xâu ký tự str_1 và str_2. Kiểm tra xem str_2 có nằm trong str_1 hay không và ngược lại
str_1 = input("Nhap vao chuoi thu nhat: ")
str_2 = input("Nhap vao chuoi thu hai: ")
if str_1 in str_2:
    print("str_1 nam trong str_2")
else:
    print("str_2 nam trong str_1")

# Bài 10: Viết chương trình nhập vào một chuỗi ký tự, trả về kết quả chuỗi mới sau khi dồn tất cả số sang bên trái
# Ví dụ: Nhập vào: “Xsn61ssakdu271626s  1231  12”
#              Trả về: “61271626123112Xsnssakdus   ”
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
tach_chuoi=chuoi_nhap_vao.split()
chuoi_ket_qua="".join(sorted(tach_chuoi))
print(f"Chuoi moi la: {chuoi_ket_qua}")