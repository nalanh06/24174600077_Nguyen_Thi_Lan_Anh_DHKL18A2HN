# Câu 1: Sử dụng vòng lặp for in ra màn hình các số nguyên dương lẻ nhỏ hơn 100
for i in range(100):
    if i % 2 == 1:
        print(i)

# Câu 2: Tính các phép tính sau
# S1 = 1 + 2 + 3 + 4 + …. + n
# S2 = 1*2*3*4*…*(n-1)
# S3 = 1 – 1/2 + 1/3 – 1/4 + …. + ((-1)**n)/n
n = int(input("Nhap so nguyen duong: "))
s_1 = 0
s_2 = 1
s_3 = 0
s_4 = 0
for i in range(1,n+1):
    s_1 = s_1 + i
for i in range(1, n):
    s_2 = s_2 * i
for i in range(1, n + 1):
    s_3 = s_3 + ((-1)**(i+1)/i)
for i in range(n + 1):
    s_4 = s_4 + i/(i+2)
print(f"S1={s_1}")
print(f"S2={s_2}")
print(f"S3={s_3}")
print(f"S4={s_4}")

# Câu 3: In 50 số đầu tiên trong dãy Fibonacci
a = 0
b = 1
n = 50
for i in range(n):
    print(a)
    sum_a_b = a + b
    a = b
    b = sum_a_b

# Câu 4: Viết chương trình nhập vào một số kiểm tra xem số đó có phải số nguyên tố hay không?
n = int(input("Nhap so can kiem tra vao n: "))
if n <= 1:
    print("Khong la so nguyen to")
else:
    k=n
    for i in range(n):
        if n%k==0 and k!=n and k!=1:
            print("Khong la so nguyen to")
            break
        k=k-1
    else:
        print("La so nguyen to")
# Câu 5:Viết chương trình nhập vào một số kiểm tra xem số đó có phải số hoàn hảo hay không?
n = int(input("Nhap so nguyen duong n: "))
so_hoan_hao = 0
for i in range(1, n):
    if n%i==0:
        so_hoan_hao = so_hoan_hao + i
if so_hoan_hao == n:
    print("La so hoan hao")
else:
    print("Khong la so hoan hao")

# Câu 6: Viết chương trình nhập vào một số kiểm tra xem số đó có phải số chính phương hay không?
n = int(input("Nhap so can kiem tra vao n: "))
if n<0:
    print(f"{n} Khong la so chinh phuong")
else:
    for i in range(n+1):
        if i*i==n:
            print(f"{n} la so chinh phuong")
            break
    else:
        print(f"{n} Khong la so chinh phuong")    
# Câu 7: Viết chương trình nhập vào n, tìm tất cả các số nguyên tố nhỏ hơn n

# Câu 8: Viết chương trình nhập vào n, tìm tất cả các số hoàn hảo nhỏ hơn n

# Câu 9: Viết chương trình nhập vào n, tìm tất cả các số chính phương nhỏ hơn n

# Câu 10: Viết chương trình nhập vào 2 số bất kì, tìm ước chung lớn nhất của 2 số đó
a = int(input("Nhap vao so nguyen duong a: " ))
b = int(input("Nhap vao so nguyen duong b: " ))
so_nho_nhat = a
if b <= a:
    so_nho_nhat = b
k = so_nho_nhat
for i in range(so_nho_nhat):
    if a % k == 0 and b % k == 0:
        print(f"{k} la uoc chung lon nhat")
        break
    k = k - 1
# Câu 11: Viết chương trình nhập vào hai số bất kì, tìm bội chung nhỏ nhất của hai số đó
a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai: "))
boi_chung_nho_nhat = a * b
for i in range(1, boi_chung_nho_nhat + 1):
  if boi_chung_nho_nhat % i == 0 and a % i == 0 and b % i == 0:
    boi_chung_nho_nhat = boi_chung_nho_nhat // i
print(f"Boi chung nho nhat la: {boi_chung_nho_nhat}")
# Câu 12:Viết chương trình nhập vào mẫu số và tử số của một phân số, trả về kết quả phân số đã tối giản
tu_so = int(input("Nhap tu so: "))
mau_so = int(input("Nhap mau so: "))
so_nho_nhat = tu_so
if mau_so <= tu_so:
    so_nho_nhat = mau_so
k = so_nho_nhat
for i in range(so_nho_nhat):
    if tu_so % k == 0 and mau_so % k == 0:
        break
    k=k-1
    tu_so_toi_gian = (tu_so // k)
    mau_so_toi_gian = (mau_so // k)
print(f"Phan so toi gian la: {tu_so_toi_gian}/{mau_so_toi_gian}")
