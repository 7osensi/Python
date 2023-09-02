# Empty list
list = [] 

# Get the number of elements from the user
TotalElements = int(input("Enter number of elements : ")) 

NumberFour = 0
for i in range(0, TotalElements):
    # Get the element from the user
    element = int(input())
    # Adding the element
    list.append(element)

print(f'Number of apperances of #4 : {list.count(4)}')