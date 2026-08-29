words = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple",
    "orange",
    "orange"
]
counts = {}
def most_common_word(words):
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    largest_count = 0
    most_com_word = None
    for word, count in counts.items():
        if count > largest_count:
            most_com_word = word
            largest_count =count
    return most_com_word
result = most_common_word(words)
print(result)
















