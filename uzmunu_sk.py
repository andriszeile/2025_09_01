import random
datora_sk = random.randint(1, 1000)
print('Es iedomājos veselu skaitli diapazonā no 1 līdz 100. Uzmini to!')
meginajumi = 0
while True:
    lietotaja_sk = int(input('Ievadi savu minējumu: '))
    meginajumi += 1
    if datora_sk > lietotaja_sk:
        print('Neuzminēji! Mans skaitlis ir lielāks.')
    elif datora_sk < lietotaja_sk:
        print('Neuzminēji! Mans skaitlis ir mazāks.')
    else:
        print('Uzminēji! Izmantoti', meginajumi,' mēģinājumi.')
        break