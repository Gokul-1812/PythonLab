sentence = input("Enter the string: ").split()

length = 0

for word in sentence:
    if len(word) > length:
        length = len(word)
c = [x for x in sentence if len(x) == length]
if len(c) > 1:
    print("Bingo")
print("Longest length: ", length)
