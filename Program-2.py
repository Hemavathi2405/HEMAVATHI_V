a = int(input("Enter value of a: "))

result = []

for num in range(1, 2 * a, 2):  
    result.append(str(num))

print(", ".join(result))
