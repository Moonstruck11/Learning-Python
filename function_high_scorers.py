def get_high_scorers(students):
    high_scorers = {}
    for student, score in students.items():
        if score >= 80:
            high_scorers[student] = score
    return high_scorers
students = {"John": 72, "Sarah": 91, "Alex": 64, "Tom": 85, "Mary": 93}
result = get_high_scorers(students)
print(result)
















