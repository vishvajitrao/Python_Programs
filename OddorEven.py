# Find entered number Even or Odd

number = int(input("Enter any number for checking odd or even:- "))

if number % 2 == 0:
    print("You entered even number:")
elif (number < 0):
	print("You entered negative number:")
else:
    print("You entered odd number:")