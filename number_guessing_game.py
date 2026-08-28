import random
number = random.randint(1, 100)
def play_game(guess):
    if guess > number:
        return 'Too high!'
    elif guess < number:
        return 'Too low!'
    else :
        return 'Correct!, You got it in', count, 'guesses!'
count = 0
while True:
    guess = int(input('Guess a number: '))
    result = play_game(guess)
    if guess == number:
        count += 1
        print(result)
        break
    else:
        count += 1
        print(result)

# BETTER SOLUTION
# import random
# 
# number = random.randint(1, 100)
#
# def play_game(guess):
#     if guess > number:
#         return 'Too high!'
#     elif guess < number:
#         return 'Too low!'
#     else:
#         return 'Correct!'
#
# count = 0
#
# while True:
#     guess = int(input('Guess a number: '))
#     count += 1
#
#     result = play_game(guess)
#     print(result)
#
#     if guess == number:
#         print('You got it in', count, 'guesses!')
#         break














