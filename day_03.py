#Day 3
#  Check if a number is a palindrome
num = int(input("Enter the number to check palindrome "))
pall = 0
b = num
while num > 0:
    rem = num % 10
    pall = pall * 10 + rem
    num = num // 10
if b == pall:
    print("The given number is pallindrome")
else:
    print("The given number isnot pallindrome")

# 2. string Find the most frequent character in a string
string = input("Enter the string: ")
result = {}
for letter in string:
    if letter in result:
        result[letter] += 1
    else:
        result[letter] = 1

max_count = float("-inf")
char = ""
for key in result.keys():#or for key in result same thing
    if max_count < result[key]:
        max_count = result[key]
        char = key
print(f"Required most frequent character in string is {char}")

# 3. string Title case a sentence without .title()
sentence = input("Enter the sentence: ")
words = sentence.split()
list = []
for word in words:
    word = word[0].upper() + word[1:]
    list.append(word)
result = " ".join(list)
print(result)

# 4. list Remove duplicates from a list without set()
given_list = [1, 2, 2, 3, "hello", "hello", 4, 1, "world", 3]
result = []
for item in given_list:
    if item not in result:
        result.append(item)
print(f"REquired list without dublicates is {result}")

# 5. dict Find the most common element in a list using a dict
items = [1, "apple", 2, "banana", "apple", 3, 1, "apple", 2, 2, "banana", 2]
result = {}
for word in items:
    if word in result:
        result[word] +=1
    else:
        result[word] = 1
max_count = float("-inf")
most_com = ""
for key in result.keys():
    if max_count < result[key]:
        max_count = result[key]
        most_com = key
print(f"Most common element in list is {most_com}:{max_count} times")


