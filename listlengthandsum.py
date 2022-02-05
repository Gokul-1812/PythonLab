l1 = [5, 7, 8, 3, 4]
l2 = [3, 4, 6, 9]

if len(l1) == len(l2):
    print(True)
else:
    print(False)

if sum(l1) == sum(l2):
    print(True)
else:
    print(False)

print(set(l1) & set(l2))
