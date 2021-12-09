word = input()

counts = {}
for letter in word:
    if letter not in counts:
        counts[letter] = 1
    else:
        counts[letter] += 1

sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse = True)
for letter, count in sorted_counts:
    print(letter, count)
