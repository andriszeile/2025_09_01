'''
Pieslēgšanās sistēmai
Lietotājs drīkst pieslēgties, ja:
•	lietotājvārds ir "admin" vai "skolotajs"
•	parole ir "1234"
👉 Uzdevums:
Izveido programmu, kas:
1.	Ievadot: lietotājvārdu un paroli
2.	Pārbauda datus
3.	Izvada: "Pieslēgšanās veiksmīga" vai "Nepareizi dati"
'''
lietotajvards = input('Ievadi lietotājvārdu: ')
parole = input('Ievadi paroli: ')
if (lietotajvards == 'admin' or lietotajvards == 'skolotajs') and parole == '1234':
    print('Pieslēgšanās veiksmīga.')
else:
    print('Nepareizi dati.')