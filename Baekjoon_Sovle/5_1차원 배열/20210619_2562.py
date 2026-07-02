n = 9
i = 0
biggest = 0
num_list = []
while i < n:
    i += 1
    N = int(input())
    if N > biggest:
        biggest = N
    num_list.append(N)

print(biggest)
print(num_list.index(biggest) + 1)