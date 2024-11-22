# Câu lệnh vòng lặp while
n = 10
while n > 2:
    print(f"chay vong lap {n}")
    n = n - 1

# Vòng lặp while cũng hỗ trợ : break, continue và else
# Break
n = 10
while n > 2:
    print(f"chay vong lap {n}")
    n = n - 1
    if n == 6:
        break
# Continue
n = 10
while n > 2:
    n = n - 1
    if n == 6:
        continue
    print(f"chay vong lap {n}")
# else
n = 10
while n > 2:
    print(f"chay vong lap {n}")
    n = n - 1
    if n == 0:
        break
else:
    print("chay cau lenh else")
# Tìm số nguyên tố lớn nhất nhỏ hơn hoặc bằng 20
n = 20
while True:
    for i in range(n):
        if n%i==0 and i!=1 and i!=n:
            n = n - 1
            break
    else:
        break
    
    if n < 1:
        break

print(f"So nguyen to la {n}")