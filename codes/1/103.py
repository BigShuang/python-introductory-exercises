punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

s = input()
for mark in punctuation:
    s = s.replace(mark, " ")

print(s)