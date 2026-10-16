"Скорость лодки в стоячей воде V км/ч, скорость течения реки U км/ч"""
"(U < V). Время движения лодки по озеру T1 ч, а по реке (против течения) — T2 ч. Определить"
"путь S, пройденный лодкой (путь = время • скорость). Учесть, что при движении против"
"течения скорость лодки уменьшается на величину скорости течения."

while True:
 try:
     V= int (input("скорость "))
     break
 except ValueError:
       print("Ошибка, нужно целое число")
while True:
 try:
     U=int (input("течение "))
     break
 except ValueError:
       print("Ошибка, нужно целое число")
while True:
 try:
     T1=int (input("время озеро "))
     break
 except ValueError:
       print("Ошибка, нужно целое число")
while True:
 try:
     T2=int (input("время река "))
     break
 except ValueError:
       print("Ошибка, нужно целое число")

if U < V:
    S1 = T1 * V
    S2 = T2 * (V - U)
    print(S1, S2)
else:
    print("Неверные значения, нужно U<V")



