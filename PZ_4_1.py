"1. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг"
"конфет."
"2. Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от"
"деления определить, имеется ли в записи числа N цифра «2». Если имеется, то"
"вывести TRUE, если нет — вывести FALSE."



"1."
while True:
    try:
     k=int(input())
     break
    except ValueError:
        print("нужно целое число")
for i in range(1, 11):
    print(i * k)


"2."
while True:
    try:
     h=int(input())
     break
    except ValueError:
        print("нужно целое число")

p=h//100
print(p)
j=(h%100)//10
print(j)
i=(h%100)%10
print(i)
if p==2:
    print("TRUE")
elif j==2:
    print("TRUE")
elif i==2:
    print("TRUE")
else:
    print("FALSE")