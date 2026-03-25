'''
Uzdevums: “Laimes automāts” (slot machine)
Izveido Python programmu, kas simulē vienkāršu spēļu automātu.
📌 Nosacījumi:
Lietotājam sākumā ir 10 monētas.
Katrs grieziens maksā 1 monētu.
Katru reizi programma izlozē 3 nejaušus skaitļus no 1 līdz 5.
Ja:
visi 3 skaitļi vienādi → lietotājs iegūst +5 monētas
2 skaitļi vienādi → +2 monētas
visi dažādi → neko neiegūst
Spēle turpinās ar while, kamēr ir monētas.
Pēc katra gājiena:
izvada izlozētos skaitļus
parāda monētu skaitu
'''
import random

monetas = 10
print('*Laimes automāts*')
print(f'Sākumā tev ir {monetas} monētas.')
while monetas > 0:
    print('\n--------------------')
    print(f'Tev ir {monetas} monētas.')
    #izvele = input('Vai griezt? (j/n): ').lower()
    #if izvele !='j':
    #    print('Spēle pārtraukta.')
    #    break
    monetas -= 1
    rezultati = []
    for i in range(3):
        sk = random.randint(1, 5)
        rezultati.append(sk)
    print(f'Rezultāts: {rezultati[0]} | {rezultati[1]} | {rezultati[2]}')
    if rezultati[0] == rezultati[1] == rezultati[2]:
        print('JACKPOT!!! +5 monētas')
        monetas += 5
    elif rezultati[0] == rezultati[1] or rezultati[1] == rezultati[2] or rezultati[0] == rezultati[2]:
        print('Divi vienādi! +2 monētas')
        monetas += 2
    else:
        print('Nav vienādi. -1 monēta')
if monetas == 0:
    print('Monētas beidzās. Spēle beigusies.')
else:
    print(f'Spēle beigusies. Pāri palika {monetas} monētas.')