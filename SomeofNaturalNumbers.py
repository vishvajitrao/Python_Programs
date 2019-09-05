# Calculate some of Natural numbers
number = int(input("Enter a positive number: "))
temp = number
if number < 0:
    print("Please Enter positive number......")
else:
    sum = 0
    while number > 0:
        sum += number
        number -= 1
    print(f"Sum of {temp} Natural Numbers is {sum}") 
