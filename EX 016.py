#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#Python Exercise 016: Create a program that reads any Real number from the keyboard and displays its Integer portion on the screen.

import math

n1 = float(input("Digite um valor: "))

c =math.floor(n1)

print("o valor digitado {} e a sua porção inteira é {}".format(n1,c))