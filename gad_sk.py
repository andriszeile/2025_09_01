import random
#random.seed(45)
print(random.random())
print(random.randrange(15))
print(random.randint(4,8))
ch = random.choice('list')
print(ch)
vardi = ['Anna', 'Juris', 'Ieva', 'Pēteris']
print(vardi)
random.shuffle(vardi)
print(vardi)

saraksts = ['Anna', 'Juris', 'Ieva', 'Pēteris']
print(random.sample(saraksts,2))

print(random.uniform(1,5))