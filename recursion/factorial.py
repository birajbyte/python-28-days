def fact(num):
    if num < 0:
        print("Enter number greater than zero")
        return None
    if  num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)
num = int(input("Enter the number to check factorial ")) 
# print(fact(num))

def multi(a,b):
    if b == 1:
        return a
    else:
        return a + multi(a,b - 1)
a = int(input("Enter the number "))
b = int(input("Enter the number "))
print(multi(a,b))

def expo(a,b):
    if b == 0:
        return 1
    else:
        return a * expo(a,b-1)
a = int(input("Enter the number "))
b = int(input("Enter the number "))
print(expo(a,b))
    