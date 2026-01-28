'''
Trijstūra eksistence
Ievade: trīs malas
Uzdevums: pārbaudi, vai no šīm malām var izveidot trijstūri.
(divu malu summai jābūt lielākai par trešo)
'''
m1 = int(input('Malas garums m1='))
m2 = int(input('Malas garums m2='))
m3 = int(input('Malas garums m3='))
if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m2 + m1:
    print('Trijstūris sanāk')
else:
    print('Trijstūris nesanāk')


