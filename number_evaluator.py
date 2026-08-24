while True:
    try:
        num = int(input('Please enter a number: '))
        if num < 0:
            print('Negative')
        elif num == 0:
            print('Zero')
        else:
            print('Positive')
        num = num % 2
        if num != 0:
            print('Odd')
            break
        elif num == 0:
            print('Even')
            break
    except:
        print('Invalid input. Please enter a number.')