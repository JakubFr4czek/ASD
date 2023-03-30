import math

def is_prime( n ):

    if n < 2: return False

    if n % 2 == 0 or n % 3 ==0: return False

    pos = 5

    while pos < int(math.sqrt(n)) + 1:

        if n % pos == 0: return False

        pos += 2

        if n % pos == 0: return False

        pos += 4
    return True
