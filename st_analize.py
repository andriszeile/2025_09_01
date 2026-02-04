'''
Ievade: stundu numurs (1–8)
Uzdevums:
•	1–4 → “rīta stundas”
•	5–7 → “pēcpusdienas stundas”
•	8 → “pagarinātā diena”
•	citādi → “nepareizs stundu numurs”
'''
st = int(input('Ievadi stundas nr. (1-8): '))
if 1 <= st <=4:
    print('Rīta stunda')
elif 5 <= st <= 7:
    print('Pēcpusdienas stunda')
elif st == 8:
    print('Pagarinātā diena')
else:
    print('Nepareizs stundas nr.')