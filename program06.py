S = input("Enter the String: ").lower()
firstCharacter = S[0]
print(firstCharacter+S[1:].replace(firstCharacter,"$"))
