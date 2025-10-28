#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

#Python Exercise 028: Write a program that makes the computer "think" of an integer between 0 and 5
#and asks the user to try to guess which number the computer chose. The program should display on the screen whether the user won or lost.

import random 

print("Vou Pensar em um numero entre 0 a 5. tente adivinhar!")

p = int(input("Em que numero eu pensei: "))

l = [0,1,2,3,4,5]

r = random.choice(l)

print("processando ...")

if p == r:
   print("Parabens, voce acertou, eu pensei no numero: {}".format(r))

else:
   print("Oh Voce Perdeu haha, eu pensei no numero: {}".format(r))

