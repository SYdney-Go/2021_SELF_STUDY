N = int(input())
numbers = list(map(int, input().split()))

biggest = max(numbers)
smallest = min(numbers)
print(smallest, biggest)


print('-----------------------')

biggest = -1000000
smallest = 1000000

for number in numbers:
    if number < smallest:
        smallest = number

for number in numbers:
    if number > biggest:
        biggest = number

print(smallest, biggest)