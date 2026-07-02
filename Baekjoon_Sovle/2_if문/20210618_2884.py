H, M = map(int, input().split())

if H-1 < 0:
    if M < 45:
        print(23, M+60-45)
    else:
        print(H, M-45)
else:
    if M < 45:
        print(H-1, M+60-45)
    else:
        print(H, M-45)