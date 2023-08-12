character = input("Enter a characters : ")

# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Check if the character is in the list
if character in vowels:
    print(True)
else:
    print(False)