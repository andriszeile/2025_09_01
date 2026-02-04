'''
Trīs skaitļu maksimums
Ievade: trīs skaitļi
Uzdevums: izvada lielāko no trim skaitļiem. Papildus: parāda ja vienādi
'''
sk1 = int(input('Ievadi sk1='))
sk2 = int(input('Ievadi sk2='))
sk3 = int(input('Ievadi sk3='))
if sk1 == sk2 == sk3:
    print('Skaitļi vienādi')
elif sk1 >= sk2 and sk1 >= sk3:
    print('Lielākais ir ',sk1)
elif sk2 >= sk1 and sk2 >= sk3:
    print('Lielākais ir ',sk2)
else:
    print('Lielākais ir ',sk3)

    