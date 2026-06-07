n = int(input("Enter the number of terms: "))

# First two terms
a, b = 0, 1

print("Fibonacci series:")

count = 0
while count < n:
    print(a, end=" ")
    # Update values
    temp = a + b
    a = b
    b = temp
    count+=1