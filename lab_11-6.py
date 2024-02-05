# Liam O'Hara
# Initialize sum
total_sum = 0

while True:
    # Prompt user for input
    user_input = input("Enter a number (or -1 to end): ")

    # Check if the input is a valid number
    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    # Check if the user wants to end the program
    if number == -1:
        break
    # Add the number to the sum
    total_sum += number
# Display the sum of all numbers entered
print(f"Sum of all numbers entered: {total_sum}")