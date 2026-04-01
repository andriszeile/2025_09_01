import random
karst = 0
tsumma = 0
for diena in range(1, 8):
    temp = random.randint(-10, 30)
    print(f'{diena}.dienas temperatūra ir {temp}')
    tsumma += temp
    if temp > 20:
        karst += 1
tvideja = tsumma / 7
print(f'Visu dienu vidējā temperatūra ir {tvideja:.1f}')
print(f'Karsto dienu skaits (>20) ir {karst}.')    