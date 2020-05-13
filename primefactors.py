factor = int(input("Enter an interger: "))
n = 2

if factor < 2:
    print("Please enter a positive interger greater than or equal to two.")

else: 
    print("The prime factors of", factor, "are:")
while n*n <= factor:
    if factor % n:
        n += 1
    else:
        factor //= n
    print(n)