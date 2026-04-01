import random

summa = 0
karstas_dienas = 0

for diena in range(1, 8):
    temperatura = random.randint(-10, 30)
    print(f"{diena}. diena: {temperatura}°C")

    summa += temperatura

    if temperatura > 20:
        karstas_dienas += 1

videja = summa / 7

print(f"\nVidējā temperatūra: {videja:.1f}°C")
print(f"Karstas dienas (>20°C): {karstas_dienas}")