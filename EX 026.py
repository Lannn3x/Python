#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

#Python Exercise 026: Write a program that reads a sentence from the keyboard and shows how many times the letter "A" appears,
#in which position it appears the first time and in which position it appears the last time.

f = str(input('Digite Uma Frase: ')).strip()

u = f.upper()

l = u.count('A')

p = u.find('A') + 1

e = u.rfind('A') + 1

print("A Letra 'A' Aparece {} Vezes Na Frase!".format(l))

print("A Primeira Letra 'A' Apareceu Na Posição {}".format(p))

print("A Ultima Letra 'A' Apareceu Na Posição {}".format(e))