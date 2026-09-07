numbers = [1, 4, 7, 10, 13, 16, 19, 22]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
squares = [number * number for number in numbers]
print(squares)
greater_than_ten = [number for number in numbers if number > 10]
print(greater_than_ten)
squares_dict = {number : number * number for number in numbers}
print(squares_dict)
squares_of_even = [number * number for number in numbers if number % 2 == 0]
print(squares_of_even)

words = ["apple", "banana", "kiwi", "watermelon", "pear", "grape"]
length_more_than_four = [len(word) for word in words if len(word) > 4]
print(length_more_than_four)