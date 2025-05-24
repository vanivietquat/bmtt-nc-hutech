import re

input_str = input("Nhập chuỗi ký tự: ")

# Tìm tất cả các số nguyên (có thể âm hoặc dương)
so_nguyen = re.findall(r'-?\d+', input_str)

# Chuyển các số tìm được thành int
so_nguyen = list(map(int, so_nguyen))

tong_duong = sum(num for num in so_nguyen if num > 0)
tong_am = sum(num for num in so_nguyen if num < 0)

print(f"Giá trị dương: {tong_duong}. Giá trị âm: {tong_am}.")
