# program to check whether a number is prime or not
import math
n = int(input())
if n <= 1:
    print("not a prime number")
elif n == 2:
    print("prime number")
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print("not a prime number")
            break
    else:
        print("prime number")
