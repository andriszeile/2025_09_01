"""
Temperatūras pārveidotājs

Ievade: grādi pēc Celsija C
Izvade: Fārenheiti 
formula konvertācijai - F = C * 9/5 + 32
"""
c = float(input('Temperatūra pēc Celsija skalas:'))
f = c * 9 / 5 + 32
print('Grādi pēc Fārentheita skalas:',f)