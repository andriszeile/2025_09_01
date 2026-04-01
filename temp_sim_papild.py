import random

summa = 0
karstas_dienas = 0
aukstaka = 30
siltaka = -10

for diena in range(1, 8):
    temperatura = random.randint(-10, 30)
    print(f"{diena}. diena: {temperatura}°C", end="")

    if temperatura < 0:
        print(" - Sals!")
    else:
        print()

    summa += temperatura

    if temperatura > 20:
        karstas_dienas += 1

    if temperatura < aukstaka:
        aukstaka = temperatura

    if temperatura > siltaka:
        siltaka = temperatura

videja = summa / 7

print(f"\nVidējā temperatūra: {videja:.1f}°C")
print(f"Karstas dienas (>20°C): {karstas_dienas}")
print(f"Aukstākā temperatūra: {aukstaka}°C")
print(f"Siltākā temperatūra: {siltaka}°C")