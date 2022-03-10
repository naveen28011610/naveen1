str=input("enter the string")
if str[::-1]==str:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")