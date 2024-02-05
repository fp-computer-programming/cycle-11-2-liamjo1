# Liam O'Hara
def find_evens(num_A, num_B):
    even_numbers = [10,20]
    for num in range(num_A, num_B):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Example usage:
num_A = 10
num_B = 20

result = find_evens(num_A, num_B)
print(f"Even numbers between {num_A} and {num_B}: {result}")