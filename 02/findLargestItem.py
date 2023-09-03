

list1 = [11,22,33,66,55,44]
print(f"largest element is {max(list1)}")

list2 = [11,22,33,44,55,66]
max = 0
for i in range(len(list2)) :
    if list2[i] > max :
        max = list2[i]
        
print(f"largest element is {max}")