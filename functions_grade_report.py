def calculate_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)
    return average

def calculate_highest(scores):
    highest_so_far = scores[0]
    for score in scores[1:]:
        if score > highest_so_far:
            highest_so_far = score
    return highest_so_far

def calculate_lowest(scores):
    lowest_so_far = scores[0]
    for score in scores[1:]:
        if score < lowest_so_far:
            lowest_so_far = score
    return lowest_so_far

def stats(scores):
    average = calculate_average(scores)
    highest = calculate_highest(scores)
    lowest = calculate_lowest(scores)
    grade = calculate_grade(average)
    return average, highest, lowest, grade

scores = [95, 82, 76, 91, 64, 88]

average, highest, lowest, grade = stats(scores)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Grade:", grade)



