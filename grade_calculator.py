name=input('What is your name?')
scr=input('What is your score?')
try:
    scr=int(scr)
except:
    print('Invalid input')
else:
    if 0<=scr<=100:
        if scr>=80:
            grade = 'A'
            print(name,', your grade is', grade)
        elif scr >= 70:
            grade = 'B'
            print(name,', your grade is', grade)
        elif scr>=60:
            grade = 'C'
            print(name,', your grade is', grade)
        elif scr>=50:
            grade = 'D'
            print(name,', your grade is', grade)
        else:
            grade = 'F'
            print(name,', your grade is', grade)
        if grade!='F':
            print('You passed!')
        else:
            print('You failed.')

