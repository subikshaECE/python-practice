# Get a number from user
n = int(input("Enter a number: "))
# Store original number
original = n
# Initialize reverse value
reverse = 0
# Reverse the number
while n > 0:
    digit = n % 10                     # Get last digit
    reverse = reverse * 10 + digit     # Build reverse number
    n = n // 10                        # Remove last digit
# Check palindrome
if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
