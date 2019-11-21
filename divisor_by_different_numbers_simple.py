import re
print("Welcome to the program, which checks the divisibility of an interval of integer numbers "
      "with the desired divisors.")
min_num = int(input("Please, enter the lower limit of the interval: ").strip().replace(",", "."))
max_num = int(input("Please, enter the upper limit of the interval: ").strip().replace(",", "."))
divisors = [int(x) for x in re.split("[\s,]+", input("Please, enter the divisors (separated by space or ,): "))]
divisors.sort()
print(f"Thank you! Here is your result, calculated on the interval [{min_num}, {max_num}]: ")
for num in range(min_num, max_num+1):
    printed = False
    for div in divisors:
        if num % div == 0:
            print(f"div{div}", end="")
            printed = True
    if not printed:
        print(num, end="")
    print()