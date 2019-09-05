# Ckeck string Palindrome or not
my_string = str(input("Enter any string wish your choice:- "))
rev_str = reversed(my_string)
if list(my_string) == list(rev_str):
    print(my_string, "is palindrome string")
else:
    print(my_string, "is not Palindrome string")