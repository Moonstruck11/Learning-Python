def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
num = int(input('Enter a number: '))
result = is_even(num)
if result == True:
    print('Number is even')
else:
    print('Number is odd')






