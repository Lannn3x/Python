#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

#Python Exercise 042: Redo CHALLENGE 035 on triangles, adding the feature of showing what type of triangle will be formed:
#EQUILATERAL: all sides equal
#ISOSCELES: two sides equal, one different
#SCALENE: all sides different


print("\033[31m -=-\033[m" * 20)

n1 = float(input("Primeiro Sergmento: \033[m"))

n2 = float(input("Segundo Sergmento: \033[m"))

n3 = float(input("Terceiro Sergmento: \033[m"))

print("\033[31m -=-\033[m" * 20)

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:

    print("Os Sergmentos Acima Podem Formar Um Triangulo !")

    if n1 == n2 == n3:
        print("Equilátero")

    elif n1 != n2 != n3 != n1:
        print("Escaleno") 

    else:
        print("Isósceles")

else:
    ("Com Esses Sergmentos Não Da Para Formar Um Triangulo !")


