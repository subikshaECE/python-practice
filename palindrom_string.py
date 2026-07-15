# Get a string from user
word = input("Enter a word: ")
# Reverse the string
reverse = word[::-1]
# Check palindrome
if word == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
