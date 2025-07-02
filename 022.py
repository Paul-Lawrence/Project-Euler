def name_score(name):
    return (sum(ord(c)-64 for c in name))

names = sorted([name.translate({ord(i): None for i in '"'}) for name in open('0022_names.txt', 'r').readlines()[0].split(',')])
namesum = sum((names.index(name)+1)*name_score(name) for name in names)
print(namesum)