"""
Laika pārveidošana sekundēs

Ievade: stundas, minūtes, sekundes
Izvade: cik kopā sekundes.
"""
h = int(input('Stundas: '))
m = int(input('Minūtes: '))
s = int(input('Sekundes: '))
kopa_s = s + m *60 + h * 3600
print('Kopā sekundes ir', kopa_s)