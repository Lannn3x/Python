#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#Python Exercise 035: Develop a program that reads the lengths of three lines and tells the user whether or not they can form a triangle.

n1 = float(input("Primeiro Sergmento: "))

n2 = float(input("Segundo Sergmento: "))

n3 = float(input("Terceiro Sergmento: "))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:

    print("Os Sergmentos Acima Podem Formar Um Triangulo !")

else:
    print("Os Sergmentos Acima Não Podem Formar Um Triangulo !")