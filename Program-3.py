a = int(input("Enter value of a: "))

if a % 2 == 0:
    n = a - 1
else:
    n = a

result = []
for i in range(n):
    num = 2 * i + 1
    result.append(str(num))

print(", ".join(result))
