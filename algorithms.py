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
