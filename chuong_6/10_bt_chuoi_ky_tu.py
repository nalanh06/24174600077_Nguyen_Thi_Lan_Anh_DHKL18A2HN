# Bài tập về chuỗi ký tự
# Dạng thứ nhất: áp dụng xử lý chuỗi ký tự bằng các phương pháp có sẵn
# Bài 1: Nhập vào một chuỗi ký tự bất kỳ. Đếm số ký tự trong chuỗi.
# Cachs 1:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
so_ky_tu_trong_chuoi = len(chuoi_nhap_vao)
print(f"So ky tu trong chuoi la {so_ky_tu_trong_chuoi}")
# Cách 2:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
dem = 0
for chu in chuoi_nhap_vao:
    print(chu)
    dem = dem + 1
print(f"So ky tu trong chuoi la {dem}")

# Bài 2: Nhap vào một chuỗi bất kỳ. Xóa các khoảng trắng ở đầu và cuối chuỗi
# Cách 1:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
chuoi_da_xoa_khoang_trong = chuoi_nhap_vao.strip()
print(f"Chuoi sau khi xoa khoang trong {chuoi_da_xoa_khoang_trong}")
# Cách 2:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
# chuoi nhap vao        
chuoi_xu_ly_dau = ""
kiem_tra_dau = False
for chu in chuoi_nhap_vao:
    if chu == " " and kiem_tra_dau == False:
        continue
    else:
        kiem_tra_dau == True
        chuoi_xu_ly_dau = chuoi_xu_ly_dau + chu
chuoi_dao_nguoc = chuoi_xu_ly_dau[::-1]
chuoi_dao_nguoc_xu_ly_dau = ""





# Bài 3: Nhập chuỗi bất kỳ. Xóa tất cả các khoảng trống thừa trong chuỗi
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
tach_chuoi = chuoi_nhap_vao.split()
chuoi_ket_qua = " ".join(tach_chuoi)
#"chuoi nhap vao"
print(f"Chuoi ket qua: {chuoi_ket_qua}")

#Cách 2: BTVN

# Dạng thứ hai: áp dụng kết hợp xử lý vòng lặp và xử lý chuỗi ký tự
# Bài 1:Nhập vào một chuỗi ký tự bất kỳ.
# Đếm xem có bao nhiêu ký tự là chữ, bao nhiêu ký tự là số và bao nhiêu ký tự đặc biệt
# isalpha(): kiểm tra chữ cái
# isdigit(): kiểm tra số
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
dem_chu = 0
dem_so = 0
dem_ky_tu_dac_biet = 0
for chu in chuoi_nhap_vao:
    if chu.isalpha() == True:
        dem_chu += 1
    else:
        if chu.isdigit() == True:
            dem_so = dem_so + 1
        else:
            dem_ky_tu_dac_biet = dem_ky_tu_dac_biet + 1
print(f"So chu cai: {dem_chu}")
print(f"So so: {dem_so}")
print(f"So ky tu dac biet: {dem_ky_tu_dac_biet}")

# Bài 2:Viết chương trình nhập vào một số kiểm tra xem số đó có phải số nguyên tố hay không?
n = input("Nhap vao so nguyen duong can kiem tra: ")




# Bài 3: Nhập vao 2 số thực bất kỳ. Tính tổng 2 số thực đó
while True:
    a = input("Nhap vao so thuc a: ")
    so_kiem_tra = a.replace(".","")
    so_kiem_tra = so_kiem_tra.replace("-","")
    if a.isdigit() == False:
        print("Gia trị nhap vao khong phai khong gian so")
    else:
        dem_dau_cham = a.count(".")
        dem_dau_gach = a.count("-")
        if dem_dau_gach > 1 or dem_dau_gach > 1:
            print("Gia trị nhap vao khong phai khong gian so")
        else:
            vi_tri_dau_gach = a.find("-")
            if vi_tri_dau_gach != 0:
                print("Gia trị nhap vao khong phai khong gian so")
            else:
                break
while True:
    b = input("Nhap vao so thuc b: ")
    so_kiem_tra = b.replace(".","")
    so_kiem_tra = so_kiem_tra.replace("-","")
    if b.isdigit() == False:
        print("Gia trị nhap vao khong phai khong gian so")
    else:
        dem_dau_cham = b.count(".")
        dem_dau_gach = b.count("-")
        if dem_dau_gach > 1 or dem_dau_gach > 1:
            print("Gia trị nhap vao khong phai khong gian so")
        else:
            vi_tri_dau_gach = b.find("-")
            if vi_tri_dau_gach != 0:
                print("Gia trị nhap vao khong phai khong gian so")
            else:
                break
a = float(a)
b = float(b)
tong = a + b
print(f"Tong hai so thuc la: {tong}")