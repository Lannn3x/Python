#Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#Python Exercise 020: The same teacher from challenge 019 wants to randomly select the order in which students will present their work.
#Write a program that reads the names of the four students and displays the order selected.

import random

a1 = str(input("Nome Do Primeiro Aluno: "))

a2 = str(input("Nome Do Segundo Aluno: "))

a3 = str(input("Nome Do Terceiro Aluno: "))

a4 = str(input("Nome Do Terceiro Aluno: "))

l1 = [a1, a2, a3, a4]

r = random.shuffle(l1)

print("A ordem Sorteada Sera: ")
print(l1)

