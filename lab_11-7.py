# Liam O'Hara
# Sample list of numbers
numbers = [1, 3, 7, 9, 12, 18, 21, 25, 30]

# Iterate through the list
for num in numbers:
    # Check if the number is not a multiple of 3
    if num % 3 != 0:
        # Skip to the next iteration
        continue
    
    # Print the number if it is a multiple of 3
    print(f"{num} is a multiple of 3")