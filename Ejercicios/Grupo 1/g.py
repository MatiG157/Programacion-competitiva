inp = []

g = int(input())
for i in range(g):
    inp.append(input())

gems = {"purple": "Power",
        "green": "Time",
        "blue":"Space", 
        "orange":"Soul", 
        "red":"Reality",
        "yellow": "Mind"}
count = 6

for gem in inp:
    if gem in gems:
        count -= 1
        del gems[gem]

print(count)
for gem in gems:
   print(gems[gem])


