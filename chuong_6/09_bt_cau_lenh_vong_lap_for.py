#In dãy số các số lẻ nhỏ hơn n
n = int(input("Nhap vao so nguyen duong n: "))
for i in range(n): #-> chuỗi chạy từ 0-> n-1
    if i%2 == 1:
        print(i)
#In n các số Fibonacci
a = 0
b = 1
n = int(input("Nhap vao so nguyen duong n: "))
for i in range(n):
    print(a)
    sum_a_b = a + b
    a = b
    b = sum_a_b

#Tính tổng các số hạng từ 1 đến n
tong_s = 0
n = int(input("Nhap vao gia tri nguyen duong n: "))
for i in range(n + 1):
    tong_s = tong_s + i
    print(f"tong_s = {tong_s}")

print(f"Tong cac so tu 1 den n {tong_s}")
#Tính giai thừa của số n (n!)
tich_p = 1
for i in range(n + 1):
    if i == 0:
        continue
    tich_p = tich_p*i
    print(f"Tich giai thua cua so n {tich_p}")
#S = 1+2+3+...+n
#Nhập vào n, tính tổng số hạng dựa theo S
#S = 1 - 1/2 + 1/3 - 1/4 + 1/5 -....
# 1/1 + (-1)*1/2 + (1)*1/3 - (-1)*1/4 +....
# ((-1)**n)*(1/n)

#Nhập vào 2 số a,b Tìm ước chung lớn nhất của hai số này
a = int(input("Nhap vao so nguyen duong a: "))
b = int(input("Nhap vao so nguyen duong b: "))
so_nho_nhat = a
if b >= a:
    so_nho_nhat = b
k = so_nho_nhat
for i in range(so_nho_nhat):
    if a % k == 0 and b % k == 0:
        print(f"{k} la uoc chung lon nhat")
    k = k - 1