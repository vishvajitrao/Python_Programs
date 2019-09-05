# Calculate list of prime numbers between two numbers

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print("List of all prime numbers between", first_number, 'and', second_number,'.')

for num in range(first_number, second_number):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)