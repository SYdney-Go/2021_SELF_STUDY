ten_num_list = []
remainder_list = []

for i in range(10):
    number = int(input())
    ten_num_list.append(number)

for j in ten_num_list:
    cal = j % 42
    if cal not in remainder_list:
        remainder_list.append(cal)

print(len(remainder_list))