case_num = int(input())
case_score = []

for case in range(case_num):
    score = 0
    test_case = input()
    test_split = test_case.split('X')
    for part in test_split:
        for i in range(1, len(part)+1):
            score += i
    case_score.append(score)

for result in case_score:
    print(result)