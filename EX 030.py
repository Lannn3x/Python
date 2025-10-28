#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

#Python Exercise 030: Create a program that reads an integer and displays on the screen whether it is EVEN or ODD.

v = int(input("Digite Um Valor Inteiro E descubra se ele é par ou impar: "))

p = v % 2

if p == 0:
    print("O Numero {} É PAR".format(v))

else:
    print("O Numero {} É Impar".format(v))