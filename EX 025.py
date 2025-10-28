#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

#Python Exercise 025: Create a program that reads a person's name and tells if they have "SILVA" in their name.

name = str(input('Qual é seu nome? ')).strip()

u = name.upper()

s = 'SILVA' in u

print('Seu  nome tem Silva? {}'.format(s))