import sys
import math
import re

print("Welcome to the program, which checks the divisibility of an interval of integer numbers "
      "with the desired divisors.")

#the following while loop reads the users entery of the interval's lower limit and
# tries to save some possible user's mistakes
correct_min = False
while not correct_min:
    min_num = input("Please, enter the lower limit of the interval: ").strip().replace(",", ".")
    try:
        min_num = int(min_num)
        if min_num < 0:
            print("ERROR: The entered lower limit is below 0. Try again!")
        else:
            correct_min = True
    except ValueError:
        try:
            min_num = math.ceil(float(min_num))
            if min_num < 0:
                print("ERROR: The entered lower limit is below 0. Try again!")
            else:
                correct_min = True
        except ValueError:
            print("SERIOUS ERROR: The entered value is not a number. Please, retry!")
            sys.exit()

#the following while loop reads the users entery of the interval's lupper limit and
# tries to save some possible user's mistakes
correct_max = False
while not correct_max:
    max_num = input("Please, enter the upper limit of the interval: ").strip().replace(",", ".")
    try:
        max_num = int(max_num)
        if max_num < min_num:
            print(f"ERROR: The entered upper limit is lower that the lower limit ({max_num} < {min_num}). Try again!")
        else:
            correct_max = True
    except ValueError:
        try:
            max_num = math.floor(float(max_num))
            if max_num < min_num:
                print(f"ERROR: The entered upper limit is lower that the lower limit ({max_num} < {min_num}). Try again!")
            else:
                correct_max = True
        except ValueError:
            print("SERIOUS ERROR: The entered value is not a number. Please, retry!")
            sys.exit()

#this part reeds the array of divisors
correct_divisors = False
while not correct_divisors:
    divisors_entry = re.split("[\s,]+", input("Please, enter the divisors (separated by space or ,): "))
    try:
        divisors = [int(x) for x in divisors_entry]
        correct_divisors = True
    except ValueError:
        print("ERROR: Not all the divisors are integer numbers! Please renter them!")

divisors.sort()
print(f"Thank you! Here is your result, calculated on the interval [{min_num}, {max_num}]: ")
#the following part checks the divisibility and returns the output in div{i}div{j} form
for num in range(min_num, max_num+1):
    printed = False
    for div in divisors:
        if num % div == 0:
            print(f"div{div}", end="")
            printed = True
    if not printed:
        print(num, end="")
    print()