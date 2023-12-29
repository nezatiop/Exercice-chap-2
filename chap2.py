import math as m
"""
nombre = float(input())
if nombre % 2 == 0:
    print("pair")
else:
    print("impair")
"""
"""
nombre = float(input())
print(abs(nombre))
"""
"""
annee = int(input())
if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    print("bissextile")
else:
    print("non bissextile")
"""
"""
nombre = int(input())
reponse = 1
while nombre != 0:
    reponse *= nombre
    nombre -= 1
print(reponse)
"""
"""
nombre = int(input())
if nombre > 1:
    for i in range(2, nombre // 2 + 1):
        if (nombre % i) == 0:
            print("est pas un nombre premier")
            break
    else:
        print("est un nombre premier")
else:
    print("pas un nombre premier")
"""