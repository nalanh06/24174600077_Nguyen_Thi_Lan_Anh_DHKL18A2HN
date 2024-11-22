# a = []
# b = ["abc"]

# Bộ nhớ của list chia sẻ cho nhau
a = 5
b = a
b = a + 1
print(a)
print(b)

# Phương thức sao lưu
a = ["abc", "def", ]
b = a.copy
b[0] = "chuoi thay doi"
print(a)
print(b)


# thay đổi giá trị trong danh sách
a = ["abc", "def", "ghijk", 1, 2, 3]
a[3] = 10 #thay thế phần tử trong danh sách
a[1:4] = [6,7,8] #thay thế phần tử trong danh sách
print(a)

# Độ dài của danh sách
print(len(a)) #kiểm tra độ dài danh sách
# các phương thức thêm và bớt
a.append("abca") #truyền 1 chuỗi ký tự vào cuối danh sách
# Thêm nhiều phần tử vào danh sách
a.extend([1,2,3])
print(a)

a.clear() # xóa tất cả các phần tử trong danh sách
a.pop() # Lấy phần tử cuối cùng ra khỏi danh sách và xóa phần tử đó ra khỏi danh sách
# ex:
a.pop() # danh sách cuối cùng trong a sẽ bị lấy ra và xóa khỏi danh sách
print(a)
print(b) # giá trị cuối cùng bị lấy ra kia sẽ là biến trong b

# Xóa 1 phần tử trong chuỗi
a.remove() # loại bỏ 1 phần tử trong danh sách điều kiện là phải ghi đúng phân tử đó

# Thêm 1 phần tử vào vị trí index
a.insert() # truyền 1 phần tử vào vị trí nhất định trong danh sách
# ex:
a.insert(3, "kkk") #thêm "kkk" vào vị trí số 3

# Đếm số lần phần tử xuất hiện
a.count()

# Đảo ngược danh sách
a.reverse()

# Trả về vị trí xuất hiện đầu tiên của phần tử trong danh sách
a.index() 

# Sắp xếp danh sách 
a.sort() # sắp xếp từ nhỏ đến lớn
a.sort(reverse=True)


# Bài tập lấy phần tử ra khỏi danh sách
b=[[1,2,[4,5,6]],"abc",[3,"rts",5]]
print(b[0][2][1]) # lấy ra số 5 thứ nhất




# Bài tập xử lý ma trận
matrix_a = [[0,1,2],
            [4,5,6],
            [7,8,9]]
n = 8
# Nhân ma trận A với n
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot]=matrix_a[hang][cot]*n
print(matrix_a)


