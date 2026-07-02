number = input()
original_number = number
count = 0

while True:
    # 한자리 수는 앞에 0 붙이기
    if len(number) == 1:
        number = '0' + number
    # 중간 단계 = 기존 수의 일의 자리 + 십의자리
    new_number = str(int(number[0]) + int(number[1]))
    number = number[-1] + new_number[-1]
    count += 1
    if number == original_number:
        print(count)
        break
