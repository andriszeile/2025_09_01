import random
meg = 0
trap = 0
ievade = input('Ievadi skailtli (1..10) vai stop: ')
while ievade != 'stop':
    merki = random.randint(1, 10)
    meg += 1
    if int(ievade) == merki:
        trap += 1
        print('Trāpijums')
    else:
        print('Garām')
        print(f'Bija {merki}')
    ievade = input('Ievadi skailtli (1..10) vai stop: ')
print(f'Mēģinājumu skaits: {meg}')
print(f'Trāpījumi: {trap}')
