# Check any number to be Aramstrong or not

number = int(input("Please enter any number to be check Armstrong or not: "))
number_length = len(str(number))
temp = number
sum = 0
if (number > 0):
    while temp > 0:
        rem = temp % 10
        sum += rem ** number_length
        temp = temp // 10
    if (number == sum):
        print(f"Your enterd number {number} is Armstrong Number:")
    else:
        print(f"Your enterd number {number} is not Armstrong Number:")
else:
    print("You entered wrong number please enter again right number:")

