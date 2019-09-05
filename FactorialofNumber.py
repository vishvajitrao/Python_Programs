# Calculate factorial of any number

number = int(input("Enter any number to calculate factorial:- "))
fact = 1
if number > 0:
    if number == 1:
        print(fact)
    for i in range(number, 1, -1):
        fact = i * fact
    print("Factorial Of", number, 'is: ', fact)

else:
    print("You entered wrong number:")
