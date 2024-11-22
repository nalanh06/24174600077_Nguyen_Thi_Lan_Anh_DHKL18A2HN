print("Hello world")

a = "Hello world"
b = 'Hello world'

c = 'Bạn A nói: "Abcd"'
d = 'Bạn A nói: "Abcd"'

#Kiểu dữ liệu tuần tự là kiểu dữ liệu có thể truy cập vào các phần tử ở trong nó
# Truy cập sử dụng index (danh mục)

print(a[4])

# [start:stop:step]
# start: vị trí ban đầu
# stop: vị trí kết thúc
# step: khoảng cách giữ các bước
print(a[1:7]) # lấy các giá trị từ stat đến stop-1
print(a[:7])
print(a[1:])
print(a[:])
# Mặc định của step luôn = 1
print(a[1:7:2])
print(a[::-1])

print(range(5)) #0,1,2,3,4,
#range cũng sử dụng start,stop,step
range(1,5,2)

for item in a:
    print(item)

# Hàm đo độ dài kiểu dữ liệu tuần tự: Len
print(len(a))
range(len(a)) #thu được chỉ mục chạy từ 0 đến len(a)-1 = 10

for i in range(len(a)):
    print(a[i])

# tính chất của kiểu dữ liệu chuỗi ký tự:
# - có thể truy cập
# - không thể chỉnh sửa
# - không thể sắp xếp

b = "Hello" + "world"
print(b)

n = input("Nhap vao so nguyen duong: ")
if n > 0:
    print("Da nhap dung so nguyen duong")

for i in range(len(a)):
    if a[i] == "a":
        c = c + i

# for i in a:
#     print(i)

# các phương thức trong xử lý chuỗi ký tự
a = "Helloworld123."
# web: python string
# Các phương thức kiểm tra (trả về cho mình true or false)
# các phương thức này sẽ thường bắt đầu bằng chữ "is"

# - kiểm tra chuỗi có alphanumeric (chỉ có ký tự số và chữ hay không)
print(a.isalnum())
# - kiểm tra chuỗi có toàn số hay ko (numeric)
print(a.isnumeric())
# - kiểm tra chuỗi có toàn chữ hay không (character)
print(a.isalpha())
# - kiểm tra chuỗi có nằm trong bẳng mã ascii hay ko
print(a.isascii())
# - kiểm tra chuỗi có phải kiểu số hay không
print(a.isdigit()) # số thông thường
print(a.isdecimal()) # số thập phân

a = "hello world"
# - kiểm tra xem chuỗi có khoảng trống hay ko
print(a.isspace())
# - kiểm tra in hoa in thường
print(a.isupper())
print(a.islower())
# - kiểm tra ký tự tồn tại trong chuỗi
print(a.find("llo"))
print(a.count("l"))
print(a.index("l"))

# phương thức biến đổi (các phương thức này trả về chuỗi ký tự, không thay đổi chuỗi ký tự ban đầu)
a = "Hello world"
# xóa ký tự đầu và cuối của chuỗi
a_sua = a.strip()
a_sua = a.lstrip()
a_sua = a.rstrip()

# thay thế ký tự bất kỳ
a_sua = a.replace("l","w")

# biến đổi viết hoa viết thường
a_sua = a.upper()
