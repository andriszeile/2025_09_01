import random

meg = 0
trap = 0

while True:
    ievade = input('Ievadi skailtli (1..10) vai stop: ')
    if ievade == 'stop':
        break
    if not ievade.isdigit():
        print('Lūdzu ievadi skaitli no 1 līdz 10')
        continue
    s = int(ievade)
    if s < 1 or s > 10:
        print('Skaitlim jābūt no 1 līdz 10')
        continue
    merki = random.randint(1, 10)
    meg += 1
    if s == merki:
        trap += 1
        print('Trāpijums')
    else:
        print('Garām')
        print(f'Bija {merki}')
print(f'Mēģinājumu skaits: {meg}')
print(f'Trāpījumi: {trap}')
