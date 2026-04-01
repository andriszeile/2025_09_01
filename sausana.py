import random

meg = 0
trapijumi = 0

ievade = input("Ievadi skaitli no 1 līdz 10 vai 'stop': ")

while ievade != "stop":
    merkis = random.randint(1, 10)
    skaitlis = int(ievade)

    meg += 1

    if skaitlis == merkis:
        print("Trāpījums!")
        trapijumi += 1
    else:
        print(f"Garām! Mērķis bija {merkis}")

    ievade = input("Ievadi skaitli no 1 līdz 10 vai 'stop': ")

print(f"\nMēģinājumi: {meg}")
print(f"Trāpījumi: {trapijumi}")