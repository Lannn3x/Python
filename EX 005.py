#Exercício Python 005: Faça um programa que leia um número Inteiro 
# e mostre na tela o seu sucessor e seu antecessor.

#Python Exercise 005: Write a program that reads an integer
# and displays its successor and predecessor on the screen.

num = int(input("Digite um número: "))

print("analisando o valor {}, seu antecessor é {} e o sucessor é {}".format(num, (num-1), (num+1)))

