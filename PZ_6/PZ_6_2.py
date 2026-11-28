'2.Дан список размера N. Найти номер его первого локального минимума (локальный'
'минимум — это элемент, который меньше любого из своих соседей).'

import random
n=[]
p=int(input())
for i in range(p):
    n.append(random.randint(0,100))

print(n)
print(min(n))