# Determine number of trailing zeros in factorial of n
# def traill(n):
#     num = 5       # it is simple trailing zero means count how many 5 are there.
#     count = 0              #number like 25,125 so that need to be handled 
#     while n // num != 0:
#         count += n // num
#         num = num * 5
#     return count
# x = int(input("Enter the number "))
# if x < 0:
#     print("Enter appropriate number non-negative")
# else:
#     y = traill(x)
#     print(y)
# Reverse only vowels in a string
# Pure thinking 
# words = list(input("Enter the string  "))
# a = []
# j = 0
# for letter in words:
#     if letter in "aeiou":
#         a.append(letter)
# b = a[::-1]
# for i in range(len(words)):
#     if words[i] in "aeiou":
#         words[i] = b[j]
#         j += 1
# result = "".join(words)
# print(result)
# # On same question with two pointer concept
# words = list(input("Enter the string  "))
# left = 0
# right = len(words) - 1
# while left < right:
#     if words[left].lower() not in "aeiou":
#         left += 1
#     elif words[right].lower() not in "aeiou":
#         right -= 1
#     else:
#         words[left],words[right] = words[right],words[left]
#         left += 1
#         right -=1
# print("".join(words))
# dict Convert two lists into a dict (keys and values)
keys = ["name", "age", "city", "job"]
values = ["Biraj", 19, "Pokhara", "Developer"]
dic = {}
if len(keys) == len(values):
    for i in range(len(keys)):
        dic[keys[i]] = values[i]
    print(dic)
else:
    print("List must me equal of length")
#one line code using zip beautiful concept
dic = dict(zip(keys,values))# it also handle the edge case if length isnot equal 
print(dic)