# Get a number from user
n = int(input("Enter a number: "))
# Store original number
original = n
# Find number of digits
count = len(str(n))
# Initialize sum
sum = 0
# Calculate sum of digits raised to power of count
while n > 0:
    digit = n % 10              # Get last digit
    sum = sum + digit ** count  # Add digit power
    n = n // 10                 # Remove last digit
# Check Armstrong number
if original == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
