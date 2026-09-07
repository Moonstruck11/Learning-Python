numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def average(numbers):
    total = 0
    amount = 0
    for num in numbers:
        total += num
        amount += 1
    average = total / amount
    return average
result1 = average(numbers)
print(result1)

def maximum(numbers):
    largest_so_far = numbers[0]
    for num in numbers:
        if num > largest_so_far:
            largest_so_far = num
    return largest_so_far
result2 = maximum(numbers)
print(result2)

def minimum(numbers):
    smallest_so_far = numbers[0]
    for num in numbers:
        if num < smallest_so_far:
            smallest_so_far = num
    return smallest_so_far
result3 = minimum(numbers)
print(result3)

def median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        middle = numbers[int(len(numbers)/2) - 1]
        aft_middle = numbers[int(len(numbers)/2)]
        median = (middle + aft_middle) / 2
    else:
        middle = numbers[(int(len(numbers) + 1) / 2 - 1)]
        median = middle
    return median
result4 = median(numbers)
print(result4)



