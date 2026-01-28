''''
Pozitīvs, negatīvs vai nulle
Ievade: skaitlis
Uzdevums: izvada, vai skaitlis ir pozitīvs, negatīvs vai 0.
'''
sk = int(input('Ievadi veselu skaitli: '))
if sk == 0:
    print('Skaitlis ir nulle')
elif sk > 0:
    print('Skaitlis ir pozitīvs')
else:
    print('Skaitlis ir negatīvs')