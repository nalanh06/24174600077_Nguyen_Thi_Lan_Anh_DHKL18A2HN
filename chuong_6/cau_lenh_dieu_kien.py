#3 kiểu viết câu lệnh điều kiện
#câu lệnh if...(sử dụng với 1 điều kiện xét)
#câu lệnh if...else(sử dụng với 1 điều kiện xét và có điều kiện)
#câu lệnh if...elif...else(sử dụng với nhiều điều kiện cần xét, )

#xử lý xoay quanh boolean(True,False)
1 > 2
1 < 2
1 >= 2
1 <= 2
1 == 2
1 != 2
"abc" == "123"
#=> trả về kết quả True, False
#Đối với if khi xét điều kiện
# - Nếu điều kiện đúng (True) thì câu lệnh của if sẽ hoạt động
# - Nếu điều kiện sai (False) thì câu lệnh if sẽ bị bỏ qua
a = 10
if a > 20:
    print("Gia tri a thoa man dieu kien")
    b = a + 1   
print("Ket thuc chuong trinh")

#Đối với câu lệnh if...else
# - Nếu điều kiện đúng (True) thì câu lệnh của if sẽ hoạt động
# - Nếu điều kiện sai (False) thì câu lệnh của else sẽ phải hoạt động
a = 10
if a > 2:
    print("Gia tri a thoa man")
else:
    print("Gia tri a khong thoa man")
print("Ket thuc chuong trinh")

#Đối với câu lệnh if...elipf...else
# - Nếu điều kiện đúng (True) thì câu lệnh của if sẽ hoạt động
# - Nếu điều kiện sai (False) thì xét điều kiện của elipf
#      +Nếu điều kiện của 
#

a = 10
if a > 0:
    print("a la so duong")
elif a < 0:
    print("a la so am")
else:
    print("a la so 0")
print("Ket thuc chuong trinh")

#x thuộc khoảng (2, 8) hợp [14, 24)
#and (và)
#or (hoặc)

c = 1
(c > 2 and c < 8) #(2, 8]
(c >= 14 and c < 24) #[14, 24)

(c > 2 and c < 8) or (c >= 14 and c < 24)
if (c > 2 and c < 8) or (c >= 14 and c < 24):
    print("Thoa man dieu kien")

if c > 2 and c <= 8:
    print("Thoa man dieu kien")
