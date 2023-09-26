s = input("Enter a word")
if s.lower() == s[::-1].lower():
    print("Palindrome")
else:
    print("Not a palindrome")
