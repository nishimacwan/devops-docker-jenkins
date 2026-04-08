import sys

if len(sys.argv) != 3:
    print("Please provide exactly two numbers")
    sys.exit(1)

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

print(num1 + num2)