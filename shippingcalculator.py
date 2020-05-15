def shippingcalculator(n):
    return (n - 1) * 2.95 + 10.95

quantity = int(input("Enter the number of items purchased: "))

print("The total shipping charge is $", shippingcalculator(quantity))