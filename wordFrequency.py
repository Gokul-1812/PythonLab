words = {}
sentence = "Coding is not about syntax. It is about the logic."

for w in sentence.lower().split():
    words[w] = words.get(w, 0) + 1

print(words)
