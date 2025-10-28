#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#Python Exercise 033: Write a program that reads three numbers and displays which is the largest and which is the smallest.

n1 = int(input("Digite O Primeiro Valor: "))

n2 = int(input("Digite O Segundo Valor: "))

n3 = int(input("Digite O Terceiro Valor: "))

menor = n1

if n2<n1 and n2<n3:
    menor = n2

if n3<n1 and n3<n2:
    menor = n3

maior = n1

if n2>n1 and n2>n3:
    maior = n2

if n3>n1 and n3>n2:
    maior = n3

    print("O Maior Valor é {}! ".format(maior))

    print("O Menor Valor é {}! ".format(menor))
