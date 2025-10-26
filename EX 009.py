#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

#Python Exercise 009: Write a program that reads any integer and displays its multiplication table on the screen.

n1 = int(input("Digite um numero para ver a tabuada: "))

print('-' * 20)

print("A Tabuada Do {} É ".format(n1))

print("{} X 1 = {}".format(n1,n1*1))
print("{} X 2 = {}".format(n1,n1*2))
print("{} X 3 = {}".format(n1,n1*3))
print("{} X 4 = {}".format(n1,n1*4))
print("{} X 5 = {}".format(n1,n1*5))
print("{} X 6 = {}".format(n1,n1*6))
print("{} X 7 = {}".format(n1,n1*7))
print("{} X 8 = {}".format(n1,n1*8))
print("{} X 9 = {}".format(n1,n1*9)) 
print("{} X 10 = {}".format(n1,n1*10))

print('-' * 20)