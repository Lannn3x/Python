#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

#Python Exercise 017: Write a program that reads the lengths of the opposite and adjacent legs of a right triangle. Calculate and display the length of the hypotenuse.

import math 

n1 = (float(input("Digite o Valor Do Cateto Oposto: ")))
    
n2 = (float(input("Digite o Valor Do Cateto Adjecente: ")))

c = math.sqrt (n1**2 + n2**2) 

print("O resultado Da Hipotenusa Deu {:.2f}".format(c))