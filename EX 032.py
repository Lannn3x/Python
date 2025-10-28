#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

#Python Exercise 032: Write a program that reads any year and shows whether it is a leap year.

from datetime import date 

a = int(input("Que Ano Voce Quer Analizar? (OBS: coloque 0 Para O Ano Atual!): "))

if a == 0:
    a = date.today().year

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("O Ano {} é Bixesto !".format(a))

else:
    print("O Ano {} Não é Bixesto !".format(a))