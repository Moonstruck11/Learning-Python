def find_smallest(numbers):
    smallest_so_far = numbers[0]
    for number in numbers:
        if number < smallest_so_far:
            smallest_so_far = number
    return smallest_so_far
numbers = [17, 4, 29, 8, 2, 11]
result = find_smallest(numbers)
print(result)














