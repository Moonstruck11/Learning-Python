numbers = [4, 7, 2, 9, 12, 5, 8]
total = 0
even_count = 0
odd_count = 0
largest_number = 0
for number in numbers:
    total += number
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    if number > largest_number:
        largest_number = number
print(total)
print(even_count)
print(odd_count)
print(largest_number)



