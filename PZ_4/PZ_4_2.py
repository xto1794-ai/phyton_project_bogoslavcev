"2. Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от"
"деления определить, имеется ли в записи числа N цифра «2». Если имеется, то"
"вывести TRUE, если нет — вывести FALSE."




while True:
    try:
        N = int (input())
        break
    except ValueError:
        print("Нужно целое число")

d = False

while N > 0:
    if N % 10 == 2:
        print(N)
        d = True
        break
    N //= 10

if d:
    print("TRUE")
else:
    print("FALSE")