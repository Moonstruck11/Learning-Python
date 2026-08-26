def analyze_numbers(numbers):
    total = 0
    even_count = 0
    largest = numbers[0]
    for number in numbers:
        total += number
        if number % 2 == 0:
            even_count += 1
        if number > largest:
            largest = number
    return total, even_count, largest
numbers = (4, 7, 2, 9, 12)
total, even_count, largest = analyze_numbers(numbers)
print('Total: ', total)
print('Even numbers: ', even_count)
print('Largest: ', largest)










