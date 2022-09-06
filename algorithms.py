# Task 1: Even or Odd
# Time Complexity: Constant - O(1)

def even_or_odd(number):
    if number % 2 == 0:
        return True
    return False


number_to_check = 4
result = even_or_odd(number_to_check)
print(f'Task 1: {number_to_check} is even - {result}')

# Task 2: Less than 100
# Time Complexity: Linear - O(n)


def list_contains_numbers_less_than_100(list_of_numbers):
    for number in list_of_numbers:
        if number >= 100:
            return False
    return True


list_of_numbers = [19, 56, 44, 99]
result = list_contains_numbers_less_than_100(list_of_numbers)
print(f'Task 2: Numbers in the list are less than 100 - {result}')

# Task 3: Repeated names
# Time Complexity: Linear - O(n)


def contains_repeated_name(list_of_names):
    all_names = []
    for name in list_of_names:
        if name in all_names:
            return True
        all_names.append(name)
    return False


names = ['Bob', 'Fred', 'Chuck', 'Fred']
result = contains_repeated_name(names)
print(f'Task 3: List contains a repeated name - {result}')


# Task 4: Sort List
# Time Complexity: Quadratic - O(n^2)

# sort list in ascending order
# cannot use built in .sort() method

def sort_list(array):
    for _ in range(len(array)):
        for index in range(len(array) - 1):
            first_number = array[index]
            second_number = array[index + 1]
            if first_number > second_number:
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp
    return array


unsorted_array = [6, 8, 3, 4, 7, 2]
sorted = sort_list(unsorted_array)
# sorted should be [2, 3, 4, 6, 7, 8]
print(f'Task 4: Sorted array is {sorted}')
