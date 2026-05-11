#Day 1
# Check if a number is prime
user_input= int(input("Enter the number  "))
if user_input>1:
    for num in range(2,user_input):
        if user_input % num == 0:
            print("The given number is not prime")
            break
    else:
        print(f"The given number {user_input} is a prime number")
else:
    print("invalid number enter value from range 2 to n")

#  2. math Find sum of all primes up to n
n=int(input("Enter the number"))
sum=0
for num in range(2,n+1):
    for i in range(2,num):
        if num%i==0:
            break
    else:    
         sum=sum+num
print(f"the required sum of prime numbers is {sum}")

#  3. string Count vowels and consonants in a string
name=input("Enter the character only")
count_vowel=0
count_consonants=0
for i in name:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":#if i in "aeiou"
        count_vowel=count_vowel+1
    else:
        count_consonants=count_consonants+1

# 4. string Reverse words in a sentence (not the letters)
sentence=input("Enter the sentence: ")
words= sentence.split()#split sentence into list with words so easy to reverse
words= words[::-1]
result=" ".join(words)#join the words form list with or without space just work as opposite of split
print(result)

# 5. dict Count word frequency in a sentence
sentence=input("Enter the sentence to count  ")
words= sentence.split()
frequency={}
for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
print(frequency)




#Some important concept for day 1
# sentence = "  Hello World Python  "

# sentence.split()          # ["Hello", "World", "Python"]     split by spaces
# sentence.split(",")       # split by comma instead
# sentence.strip()          # "Hello World Python"             remove edge spaces
# sentence.lower()          # "  hello world python  "
# sentence.upper()          # "  HELLO WORLD PYTHON  "
# sentence.replace("o","0") # "  Hell0 W0rld Pyth0n  "
# sentence.startswith("He") # False (has leading space)
# sentence.count("l")       # 3
# sentence.find("World")    # 8  (index where it starts, -1 if not found)
# " ".join(["a","b","c"])   # "a b c"   opposite of split