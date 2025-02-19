import sys

def is_prime(num):

    if num <= 1:

        return False

    for i in range(2, int(num**0.5) + 1):

        if num % i == 0:

            return False

    return True
    
n = int(sys.argv[1])
divisor = 2
counter = 0


for i in range(541):
    if counter == n:
        break
    if is_prime(i):
        print(i)
        counter = counter + 1
    else:
        continue