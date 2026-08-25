words = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)





