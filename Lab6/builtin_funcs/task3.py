s = input()

if (s == ''.join(reversed(s))):
    print("The string is palindrome.")
else:
    print("The string is not a palindrome.")