# Program to calculate average of numbers

# Take how many numbers user wants to enter
n = int(input("Enter how many numbers: "))

total = 0

# Loop to take inputs
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    total += num

# Calculate average
average = total / n

# Display result
print("Average is:", average)
