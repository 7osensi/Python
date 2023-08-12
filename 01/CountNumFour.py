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
    # Check if the number is 4
    if element == 4:
        NumberFour += 1
# Print the list
print("The list:",list)
# Print 
print("The number of appearances of number 4 in the list:",NumberFour)