# Day 15
# 1.Remove all duplicate characters from a string
#manual way
word = input("Enter the string  ").lower()
result = ""
for i in word:
    if i not in result:
        result += i
print(result)
#pythonic way
result1 = "".join(dict.fromkeys(word))#dict.fromkeys() make key with value none as key are unique 
print(result1)#join can also be used for dic too hehe

# 2.Find keys with the maximum value in a dict
dic = marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 92,
    "Eve": 88
}
lis = [] #direc without list max(dic.values())give outptu same as list without indexing as cannot be used
for value  in dic.values():
    lis.append(value)
    result = max(lis)  #dic.values()
for key,value in dic.items():# dict_values([85, 92, 78, 92, 88])
    if value == result:
        print(f"{key}:{value}")


