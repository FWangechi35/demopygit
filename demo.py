names = ("Alice", "Bob", "Charlie")
comps = ("Engineer", "Designer", "Manager")

zipped = set(zip(names, comps))
for (a,b) in zipped:
    print(a, b) 