letters = {}
word = "Magnificent"

for w in word.lower():
    letters[w] = letters.get(w, 0) + 1

print(letters)
