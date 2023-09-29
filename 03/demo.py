# mylist = [1, 2 , 5, 'N', "Hussien", 1.6]

# mylist2 = [6, 8 , 5101]

# x = "Hussein"

# for i in mylist:
#     print(i)

# print(f'length : {len(mylist)} {x}')

# mylist.extend(mylist2)

# mylist.reverse()


# print(mylist)


# color = ['Red', 'Green', 'Blue']

# with open('abc.txt', "w") as myFile: # as alias 
#     myFile.write(" ".join(color))


# content = open('abc.txt')
# print(content.read())

# # x = 10
# try:
#     print(x)
# except ArithmeticError:
#     print("Arithmatic error")
# except NameError:
#     print("Name error, x is not defined")


# if __name__ == "__main__":
#     print("I'm right")

def func(x):
    x = 5
    print("In func", x)
    print("In func", id(x))
    print("--------------------")
    

x = 10


print("Before func", x)
print("Before func", id(x))
print("--------------------")

func(x)


print("After func", x)
print("After func", id(x))