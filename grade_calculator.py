import random
num = random.randint(1,100)
attempts = 0
while num>0:
    try:
        guess = int(input('Guess a number between 1 and 100'))
        if guess<1 or guess>100:
            print('Please enter a number between 1 and 100')
            continue
    except:
        print('Invalid input')
        continue
    if guess > num:
        attempts = attempts + 1
        print('Too high!')
        continue
    if guess < num:
        attempts = attempts + 1
        print('Too low!')
    if guess == num:
        attempts = attempts + 1
        print(('Correct!'))
        print('You got it in', attempts, 'attempts')
        break




