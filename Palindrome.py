# Check number palindrome or not

number = int(input("Please enter any number to be check Palindrome or not: "))
temp = number
sum = 0
if (number > 0):
    while temp > 0:
        rem = temp % 10
        sum = (sum * 10 ) + rem 
        temp = temp // 10
    if (number == sum):
        print(f"Your enterd number {number} is Palindrome Number:")
    else:
        print(f"Your enterd number {number} is not Palindrome Number:")
else:
    print("You entered wrong number please enter again right number:")

