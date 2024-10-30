# 1. Tính năm nhuận. Năm thứ n là nhuận nếu nó chia hết cho 4, nhưng không chia hết cho 100 hoặc chia hết 400. 
n = int(input("Nhap nam:"))
if (n / 4 and n % 100) or (n / 400):
    print("Nam nhuan")
else:
    print("Nam khong nhuan")

# 2. Viết chương trình kiểm tra xem điểm M(x,y) có nằm trong hình tròn tâm I(a,b) và bán kính 
# R bằng cách xuất ra giá trị True nếu điểm M nằm trong hoặc trên hình tròn và False nếu nằm ngoài hình tròn, 
# với x, y, a, b, R nhập vào từ bàn phím?
print("Nhap vao M")
x = input("x = ")
y = input("y = ")
print("Nhap vao I")
a = input("a = ")
b = input("b = ")
x = float(x)
y = float(y)
a = float(a)
b = float(b)
r = float(input("Nhap vao R:"))
do_dai_IM = ((x-a)**2 +(y-b)**2)**(1/2)
if (do_dai_IM <= r):
    print("True")
else:
    print("False")

# 3. Viết chương trình tìm số lớn nhất trong 3 số bằng Python
x = float(input("Nhap so:"))
y = float(input("Nhap so:"))
z = float(input("Nhap so:"))
if x > y and x > z:
    print("x la so lon nhat")
if y > x and y > z:
    print("y la so lon nhat")
if z > x and z > y:
    print("z la so lon nhat")
print("Ket thuc chuong trinh")

# 4. Viết chương trình nhập vào các số a, b, c, sau đó kiểm tra bộ ba số a, b, c vừa nhập vào 
# là bộ ba cạnh của tam giác thường, tam giác vuông, tam giác cân, tam giác vuông cân, tam giác đều 
# hay không phải là bộ ba cạnh của tam giác.
a = float(input("Nhap do dai canh a="))
b = float(input("Nhap do dai canh b="))
c = float(input("Nhap do dai canh c="))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("La bo ba cua tam giac thuong")
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("La bo ba cua tam giac vuong")
    if (a == b) or (a == c) or (b == c):
        print("La bo ba cua tam giac can")
    if ((a**2 + b**2 == c**2) and (a == b)) or ((a**2 + c**2 == b**2) and (a == c)) or ((b**2 + c**2 == a**2) and (b == c)):
        print("La bo ba cua tam giac vuong can")
    if (a == b == c):
        print("La bo ba cua tam giac deu")
else:
    print("Khong la bo ba cua tam giac")
print("Ket thuc chuong trinh")

# 5. Viết chương trình kiểm tra một ký tự trong bảng chữ cái tiếng anh là nguyên âm hay phụ âm. 
# Ký tự là bất kỳ được nhập từ bàn phím.


# 6. Viết chương trình thể hiện menu lựa chọn gồm các thể loại phim hiện đang có trong rạp chiếu phim ABC. 
# Yêu cầu người dùng nhập lựa chọn thể loại phim muốn xem (Phim tình cảm, Phim kinh dị, Phim hoạt hình, Phim khoa học viễn tưởng)
print("--The loai phim--")
print("1. Phim tinh cam ")
print("2. Phim kinh di")
print("3. Phim hoat hinh")
print("4. Phim khoa hoc vien tuong")
lua_chon = input("Nhap lua chon phim muon xem (1-4):")
if lua_chon == "1":
    print(f"Xem phim tinh cam")
elif lua_chon == "2":
    print("Xem phim kinh di")
elif lua_chon == "3":
    print("Xem phim hoat hinh")
elif lua_chon == "4":
    print("Xem phim khoa hoc vien tuong")
else:
    print("Lua chon khong hop le")

# 7. Viết chương trình giải hệ phương trình 2 ẩn:
# 	    a_1*x + b_1*y = c_1
#       a_2*x + b_2*y = c_2
# Các hệ số a1, a2, b1, b2, c1, c2 nhập từ bàn phím. Xét tất cả các trường hợp cụ thể
# Công thức Cramer2 dùng tính hệ phương trình 2 ẩn
a_1 = float(input("Nhap vao he so a1:"))
a_2 = float(input("Nhap vao he so a2:"))
b_1 = float(input("Nhap vao he so b1:"))
b_2 = float(input("Nhap vao he so b2:"))
c_1 = float(input("Nhap vao he so c1:"))
c_2 = float(input("Nhap vao he so c2:"))
det_A = a_1 * b_2 - b_1 * a_2
if det_A != 0:
    det_A_1 = c_1 * b_2 - b_1 * c_2
    det_A_2 = a_1 * c_2 - c_1 * a_2
    x = det_A_1 / det_A
    y = det_A_2 / det_A
    print(f"x= {x}")
    print(f"y= {y}")
else:
    print("Phuong phap cramer2 khong kha thi")

# 8. Viết chương trình phân loại sinh viên dựa vào kết quả điểm học tập. 
# Nếu điểm A thì phân loại là sinh viên xuất sắc, 
# điểm B là sinh viên loại giỏi, 
# điểm C là sinh viên loại khá, 
# điểm D là sinh viên loại trung bình, 
# điểm E là sinh viên loại yếu, 
# điểm F là sinh viên xếp loại kém.
diem = input("Nhap ket qua diem hoc tap (A-F):")
if diem == "A":
    print("Sinh viên xuất sắc")
elif diem == "B":
    print("Sinh viên loại giỏi")
elif diem == "C":
    print("Sinh viên loại khá")
elif diem == "D":
    print("Sinh viên loại trung bình")
elif diem == "E":
    print("Sinh viên loại yếu")
else:
    print("Sinh viên xếp loại kém")

# 9. Tính cước tacxi: 
# Viết chương trình tính cước taxi theo biểu phí cơ bản như sau:
# -	Loại xe 4 chỗ
#   Giá mở cửa			11.000 đồng/0.8km
#   Trong phạm vi 20km 	12.100đ/km
#   Từ km thứ 21 trở đi 		10.000 đồng/km
# -	Loại  xe 7 chỗ
#   Giá mở cửa			13.000 đồng/0.8km
#   Trong phạm vi 30km 	14.100đ/km
#   Từ km thứ 31 trở đi 		12.000 đồng/km
# Tiền chờ: 05 phút đầu được miễn phí, từ phút thứ sáu trở đi là 800đ/phút.
# Loại xe chỉ nhập 4 hoặc 7.
loai_xe = float(input("Nhap loai xe taxi (4 or 7):"))
t = float(input("Nhap thoi gian cho (phut):"))
km_di = float(input("Nhap quang duong di (km):"))
if loai_xe == 4:
    if km_di <= 0.8:
        cuoc = 11000 
    elif km_di <= 20:
        cuoc = 11000 + (km_di - 0.8) * 12100
    else:
        cuoc = 11000 + (20 - 0.8) * 12100 + (km_di - 20) * 10000
else:
    if km_di <= 0.8:
        cuoc = 13000
    elif km_di <= 30:
        cuoc = 13000 + (km_di - 0.8) * 14100
    else:
        cuoc = 13000 + (30 - 0.8) * 14100 + (km_di - 30) * 12000
if t <= 5:
    tien_cho = 0 
else:
    tien_cho = (t - 5) * 800
tong_cuoc_taxi = cuoc + tien_cho 
print(f"Cuoc taxi la:{tong_cuoc_taxi} dong")

# 10. Viết chương trình nhập lương nhân viên, tính thuế thu nhập và lương ròng (số tiền
# lương thực sự mà nhân viên đó nhận được).
# Với các thông số giả sử như sau
# • 30% thuế thu nhập nếu lương là 15 triệu.
# • 20% thuế thu nhập nếu lương từ 7 đến 15 triệu.
# • 10% thuế thu nhập nếu lương dưới 7 triệu.
luong = float(input("Nhap tien luong cua nhan vien:"))
if luong > 15000000:
    thue_thu_nhap = luong * 0.3
elif 7000000 <= luong <=15000000:
    thue_thu_nhap = luong * 0.2
else:
    thue_thu_nhap = luong * 0.1
luong_rong = luong - thue_thu_nhap
print(f"Thue thu nhap la:{thue_thu_nhap}")
print(f"Luong rong la:{luong_rong}")