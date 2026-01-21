print('Sveika pasaule!')
a = int(input('Ievadi skaitli a='))
print('datu tips mainīgajam a:',type(a))
b = int(input('Ievadi skaitli b='))
print('datu tips mainīgajam b:',type(b))
c = a + b
print('datu tips mainīgajam c:',type(c))
print('Skaitļu summa ir c=',c)
"""
print() - konsolē parāda argumentā 
    norādīto virkni vai mainīgā vērtību
input() - atgriež mainīgajam no tastatūras
    ievadīto virknes vērtību, argumentā
    var norādīts paskaidrojuma virkni
int() - pārvērš argumentu veselā skaitlī,
    ja iespējams
float() - pārvērš argumentu decimālskaitlī,
    ja iespējams
bool() - pārvērš argumentu loģiskajā vērtībā,
    ja iespējams (0, 1, True, False)
str() - pārvērš argumentu virknē, ja iespējams
type() - nosaka un atgriež mainīgā klasi (tipu)
"""