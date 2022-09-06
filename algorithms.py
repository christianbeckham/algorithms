# Task 1: Even or Odd
# Time Complexity: Constant - O(1)

def even_or_odd(number):
    if number % 2 == 0:
        return True
    return False


number_to_check = 4
result = even_or_odd(number_to_check)
print(f'Task 1: {number_to_check} is even - {result}')
