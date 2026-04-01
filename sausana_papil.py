import random

meg = 0
trapijumi = 0

ievade = input("Ievadi skaitli no 1 līdz 10 vai 'stop': ")

while ievade != "stop":
    skaitlis = int(ievade)
    merkis = random.randint(1, 10)

    meg += 1

    if skaitlis == merkis:
        print("Trāpījums!")
        trapijumi += 1
    else:
        print(f"Garām! Mērķis bija {merkis}")

    ievade = input("Ievadi skaitli no 1 līdz 10 vai 'stop': ")

if meg > 0:
    precizitate = trapijumi / meg * 100
else:
    precizitate = 0

print(f"\nMēģinājumi: {meg}")
print(f"Trāpījumi: {trapijumi}")
print(f"Precizitāte: {precizitate:.1f}%")

if precizitate > 50:
    print("Labs šāvējs!")