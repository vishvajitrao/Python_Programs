# Calculate table of any number 

number = int(input("Enter number to find table:- "))

if number>0:
    for i in range(1,11):
        print(number, '*', i, "=", number*i)
elif(number < 0):
    print("Dear You entered negative number:")
else:
    print("Dear you enter wrong number:")