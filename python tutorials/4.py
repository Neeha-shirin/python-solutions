#prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print( "prime number")
else:
    print(" not a prime number.")
