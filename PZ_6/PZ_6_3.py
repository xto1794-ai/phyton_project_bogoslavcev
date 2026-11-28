'3.Дан список размера N (N — четное число). Поменять местами его первый элемент'
'со вторым, третий — с четвертым и т. д.'

import random
n=[]
p=int(input())

while True:
    l=p % 2
    if l==0:
        for i in range(p):
            n.append(random.randint(0,100))
        break
    else:
        p=int(input())

print(n)

i=0
while i<p:
    n[i],n[i+1]=n[i+1],n[i]
    i+=2
print(n)