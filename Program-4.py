value = input("Enter value: ").strip()
number = list(map(int, value.split()))

count = {i: 0 for i in range(1, 10)}

for num in number:
    for divisor in range(1, 10):
        if num % divisor == 0:
            count[divisor] += 1

print(count)
