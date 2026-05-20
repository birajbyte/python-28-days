# Day 10
# 1.Find the intersection of two lists without set()
# list1 = [3, 4, 5, 6, 7]
# list2 = [1, 2, 3, 4, 5]
# lis = []

# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i] == list2[j] and list[i] not in lis:
#             lis.append(list1[i])#line written for duplicate 
#             #edge case 
# print(lis)

# 2. dict Sort a dictionary by its values
# dic= {"Alice":82,"Bob":90,"Ram":70,"Shyam":30}
# result = {}
# lis = []
# for value in dic.values():
#     lis.append(value)
# lis = sorted(lis)
# for i in range(len(lis)):
#     for key in dic.keys():#without .keys also it acess key
#         if dic[key] == lis[i]:
#             result[key] = lis[i]
# print(result)
# print ascii uppercase with ord()
import string#ord give it's value manage by python
for letter in string.ascii_uppercase:
    print(f"{letter} has a value of {ord(letter)}")
print()
#  print ascii lowercase with ord()
for letter in string.ascii_lowercase:
    print(f"{letter} has a value of {ord(letter)}")  
print()
#  print ascii_letters this gives all alphates capital first
for letter in string.ascii_letters:
    print(f"{letter} has a value {ord(letter)}")


