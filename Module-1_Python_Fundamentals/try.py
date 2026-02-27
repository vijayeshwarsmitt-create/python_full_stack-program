# print("python is \tprograming language")

# my_dict={
#     "name":"sriram",
#     "age":21,
#     "gender":"male"
# }
# print(my_dict)

# my_dict["name"]="sowndhar"
# print(my_dict)

# print(5>2)
# import random
# for i in range(10):
#     print(random.random())
# x=random.random()
# if x > 0.5:
#     print("heads")
# else:
#     print("tails")

# a= 10
# b=3
# print(a&b)
a='''
a=10
b=10
print(a is b)



# list comprehension
squares = [x**2 for x in range(10)if x%2==0]
print(squares)

'''

# print(a)

# def add(a,b):
#     return a+b

# print(add(1,2))

#lambda functio
# x = lambda a,b: a+b
# print(x(1,2))

# x="Sriram"
# # print(x[1:100])
# print(x.startswith("Sr"))

# a="apple,bannana,orange"
# print(a.split(","))
# print("-".join(a.split(",")))

from pathlib import Path

# Get the directory of the current script to ensure relative paths work correctly
SCRIPT_DIR = Path(__file__).parent
FILE_PATH = SCRIPT_DIR / "sample.txt"

try:
    # 1. Critical code that might fail
    file = open(FILE_PATH, "r")
except FileNotFoundError as e:
    # 2. Handles a specific error
    print(f"Error: {e}")
else:
    # 3. Runs ONLY if the 'try' block succeeded
    print("File read successfully.")
finally:
    # 4. ALWAYS runs (Used for cleanup like closing files/DBs)
    print("Execution finished.")

numbers = [1, 2, 3, 4, 5]
target = 6

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    # This runs only if the loop finishes without a 'break'
    print(f"Target {target} was NOT found in the list.")








