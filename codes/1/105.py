line = input()
words = line.split()

longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)
