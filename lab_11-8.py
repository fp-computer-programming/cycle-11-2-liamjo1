# Liam O'Hara
def length_multiples(input_list):
    new_list = [value * index for index, value in enumerate(input_list)]
    return new_list

# Test case 1: Contains only integers
test_list1 = [1, 2, 3, 4, 5]
result1 = length_multiples(test_list1)
print("Test Case 1:", result1)

# Test case 2: Contains integer and float values
test_list2 = [1, 2.5, 3, 4.2, 5]
result2 = length_multiples(test_list2)
print("Test Case 2:", result2)

# Test case 3: Contains only strings
test_list3 = ["a", "b", "c", "d", "e"]
result3 = length_multiples(test_list3)
print("Test Case 3:", result3)