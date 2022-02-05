names = {26: "Athul", 15: "Joel", 27: "Aswanth", 19: "Gokul"}

asc_names = {n: names[n] for n in sorted(names)}
dsc_names = {n: names[n] for n in sorted(names, reverse=True)}
print(asc_names)
print(dsc_names)
