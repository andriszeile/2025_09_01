'''
uzdevums – Atlaide veikalā
Pircējs saņem atlaidi, ja:
•	pirkuma summa ir vismaz 50 €
•	vai viņam ir klienta karte
📌 Noteikumi:
Ja ir gan summa ≥ 50 un ir karte → 20% atlaide
Ja tikai viens no nosacījumiem → 10% atlaide
Ja neviens → 0%
'''
summa = float(input('Ievadi pirkumu summu: '))
karte = input('Vai ir klienta karte? (j/n): ')
if summa >= 50 and karte == 'j':
    atlaide = summa * 0.2
elif summa >= 50 or karte == 'j':
    atlaide = summa * 0.1
else:
    atlaide = summa * 0
maksat = summa - atlaide
print('Par pirkumiem jāmaksā',maksat)