# Day 12
# Find all duplicates in a list
lis = [1,2,3,2,3,2,4,5,2]
dis = {}
for num in lis:
    if num in dis:
        dis[num] +=1
    else:
        dis[num] = 1
for key,value in dis.items():
    if value > 1:
        print(f"Duplicate number {key} and  appears {value} time")
#more pythonic way
dic = {}#same as line 5,6,7,8,9 line but more clean way
for num in lis:
    dic[num] = dic.get(num,0) + 1
print(dic)

# 2.  Move all zeros to the end without sort()
input_list =  [1, 0, 3, 0, 5, 0, 2]
list1 = []
list2 = []
for num in input_list:
    if num == 0:
        list2.append(num)
    else:
        list1.append(num)
print(f"Requried list with all zeros at end {list1+list2}")

