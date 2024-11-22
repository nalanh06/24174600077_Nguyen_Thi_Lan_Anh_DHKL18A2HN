#Vòng lặp trong python
#Vòng lặp có giới hạn (vòng lặp for)
#Các kiểu dữ liệu tuần tự: string, list, tuple, set, dictionary
# range()
n = input()
for abc in range(10):
    print(abc)
#rang(10) -> 0,1,2,3,4,5,6,7,8,9
#range khi truyền giá trị mặc định yếu cầu phải là giá trị nguyên dương
#các giá trị trong range sec chạy từ 0 đến n-1

#Khi sử dụng vòng lặp nên kết hơpj với câu lệnh điều kiện
#Khi sử dụng vòng lặp nên có ục đích rõ ràng

#Trong python vòng lặp cung cấp cho người dùng 3 công thức: break, continue, else
#break: Dừng vòng lặp ngay lập tức
for i in range(10):
    if i == 4:
        break
    print(i)
#continue: Vòng lặp sẽ bỏ qua vòng lần lặp mà ở đấy xuất hiện continue
#else: Vòng lặp sẽ chạy các câu lệnh xử lý của else trong trường hợp vòng lặp ko bắt gặp break
