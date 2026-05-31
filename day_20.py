# Find all divisors of a number
num = int(input("Enter the number to find divisor "))
if num > 0:
    result = []
    for num1 in range(1,num+1):
        if num % num1 == 0:
            result.append(num1)
    print(f"Required divisor are {result}")
else:
    print("Enter the positive number")
# Find the difference between two lists (not in common)
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
result = []
for num in a:
    if num not in set(b):
        result.append(num)
for num in b:
    if num not in set(a):
        result.append(num)
print(result)
# Find the product of all elements except self (no division)
a = [1, 2, 3, 4]
result = []
for i in range(len(a)):
    product = 1
    for j in range(len(a)):
        if j != i:
            product = product * a[j]
    result.append(product)
print(result)

 
