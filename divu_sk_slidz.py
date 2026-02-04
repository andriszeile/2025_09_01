'''
Lielākais no diviem skaitļiem
Ievade: divi veseli skaitļi
Uzdevums: izvada lielāko skaitli vai paziņo, ka tie ir vienādi.
'''
sk1 = int(input('Ievadi sk1='))
sk2 = int(input('Ievadi sk2='))
if sk1 > sk2:
    print('Lielākais ir ',sk1)
elif sk2 > sk1:
    print('Lielākais ir ',sk2)
else:
    print('Skaitļi ir vienādi')