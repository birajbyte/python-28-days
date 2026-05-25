# Day 13 

# 1.dict Find top 3 most frequent words in a paragraph
paragraph = "My name is biraj. My hobby is to write code. My pupet name is raj."
words = paragraph.split()
dic = {}
lis = []
# print(words)
for word in words:
     dic[word] = dic.get(word,0) + 1 # pythonic way simple clean
    # if word in dic:
    #     dic[word] += 1
    # else:
    #     dic[word] = 1
print(dic)
for value in dic.values():
     lis.append(value)
lis = sorted(lis)
print(lis)
for num in range(-1,-4,-1):
     for key,value in list(dic.items()):
          if value == lis[num]:
               print(f"{key}:{value}")
               dic.pop(key,None)
               break
# Problem solved using standard libraray
from collections import Counter

paragraph = "My name is biraj. My hobby is to write code. My pupet name is raj."
words = paragraph.split()

counter = Counter(words)
print(counter.most_common(3))  # Top 3 automatically

#2.math Check if a number is a perfect square without sqrt()\
#perfect square mean having whole number square 2**2 == 4
number = int(input("Enter the number"))
for num in range(1,number):
     if num ** 2 == number:
          print("Given number is perfect square")
          break
else:
     print("Not a perfect square")
# Standar libraby way to get optimal solution with less time 
import math

number = int(input("Enter the number: "))
limit = int(math.sqrt(number)) + 1

for num in range(1, limit):  # much smaller range
    if num ** 2 == number:
        print("Perfect square")
        break
else:
    print("Not a perfect square")
     
