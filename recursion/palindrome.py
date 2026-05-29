# Palindrome check using recusion
#if a string is palindrome its first and last char match and last ramain charcter is <=1
def palindrome(b):
    if len(b) <= 1:
        print("palindrome")

    elif b[0] == b[-1]:
        palindrome(b[1:-1])
    else:
        print("NOt Pallindrome")
x = input("Enter the string to check")
palindrome(x)

#Reverse using recursion
# def rev(a):
    
#     if len(a) == 1:
#         return a
#     else:
#         return a[-1] + rev(a[:-1])
# a = input("Enter the string")
# print(rev(a))