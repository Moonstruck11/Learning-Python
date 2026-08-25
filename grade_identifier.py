students = {"John": 82, "Sarah": 91, "Alex": 76, "Tom": 88}
print(students)
total = 0
highest = students['John']
for name, grade in students.items():
    total += grade
    if grade > highest:
        highest = grade
    average = total / len(students)
print(average)
print(highest)
for name, grade in students.items():
    if grade == highest:
        print(name)


