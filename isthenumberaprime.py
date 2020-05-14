def prime(n):
    if n <=1:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True

number = int(input("Enter an interger: "))
if prime(number):
    print("This number is a prime number.")
else:
    print("This number is not a prime number.")