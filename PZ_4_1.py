"1. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг"
"конфет."





i=0
while True:
    try:
     k=int(input())
     break
    except ValueError:
        print("нужно целое число")
while i<=10:
    s=k*i
    print(s)
    i+=1





