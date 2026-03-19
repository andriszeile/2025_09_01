import random
no = 1
lidz = 100
print('Iedomājies veselu skaitli diapazonā no',no,'līdz',lidz)
meginajumi = 0
while True:
    #minejums = (no + lidz) // 2
    minejums = random.randint(no, lidz)
    meginajumi += 1
    print('Vai iedomātais skaitlis ir',minejums)
    atbilde = input('(L)ielāks, (M)azaks vai (U)zminēts').lower()
    if atbilde == 'l':
        no = minejums
    elif atbilde == 'm':
        lidz == minejums
    else:
        print('Uzminēju skaitli no',meginajumi,'reizēm.')
        break
