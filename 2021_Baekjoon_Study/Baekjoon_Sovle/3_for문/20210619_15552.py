import sys
T = int(input())
C = []

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    C.append(A + B)

for j in C:
    print(j)