#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

#Python Exercise 019: A teacher wants to randomly select one of his four students to erase the board.
#Write a program that helps him by reading the students' names and writing the chosen one's name on the screen.

import random

a1 = str(input("Nome Do Primeiro Aluno: "))

a2 = str(input("Nome Do Segundo Aluno: "))

a3 = str(input("Nome Do Terceiro Aluno: "))

a4 = str(input("Nome Do Terceiro Aluno: "))

l1 = [a1, a2, a3, a4]

r = random.choice(l1)

print('O Aluno Sorteado Foi: {}'.format(r))