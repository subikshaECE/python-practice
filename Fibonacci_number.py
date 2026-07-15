# Get number of terms from user
N = int(input("Enter number of terms: "))
# Initialize first two numbers
A = 0
B = 1
# Generate Fibonacci series
for i in range(N):
    print(A)
    # Find next number
    C = A + B
    # Update values
    A = B
    B = C
