#my first attempt
# while True:
#     track = list()
#     try:
#         n = int(input('Please enter a number: '))
#         for i in range(0, n):
#             total = n - i
#             track.append(total)
#         cumulative = sum(track)
#         print('Sum: ', cumulative)
#         if n % 2 == 0:
#             print('Even: ', int(n / 2))
#             print('Odd: ', int(n / 2))
#             break
#         else:
#             print('Even: ', int((n - 1) / 2))
#             print('Odd: ', int((n + 1) / 2))
#             break
#     except ValueError:
#         print('Invalid input. Please input a number.')

#my second attempt after getting hints
while True:
    try:
        n = int(input('Please enter a number: '))
        total = 0
        even_count = 0
        odd_count = 0
        for i in range(1, n + 1):
            total += i
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        print('Sum: ', total)
        print('Even numbers: ', even_count)
        print('Odd numbers: ', odd_count)
        break
    except ValueError:
        print('Invalid input. Please enter a number.')