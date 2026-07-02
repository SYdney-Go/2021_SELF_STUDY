all = []
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        C = A + B
        all.append(C)

for i in all:
    print(i)