import sys

# Total number of arguments
n = len(sys.argv)

print(f"\nTotal number of arguments passed : {n}")

# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")

for i in range(1, n):
    print(sys.argv[i], end = " ")

print("\n")