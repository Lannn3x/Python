#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

#Python Exercise 023: Write a program that reads a number from 0 to 9999 and displays each of the digits separately on the screen.

n1 = int(input('Informe Um Numero Inteiro: '))

u = n1 // 1 % 10

d = n1 // 10 % 10

c = n1 // 100 % 10

m = n1 // 1000 % 10

print("Unidade {}".format(u))
print("Dezena {}".format(d))
print("Centena {}".format(c))
print("Milhar {}".format(m))