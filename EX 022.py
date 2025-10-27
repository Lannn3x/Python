#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 

#Python Exercise 022: Create a program that reads a person's full name and displays:

name = str(input('Digite seu nome: ')).strip()

n1 = name.upper()

n2 = name.lower()

n4 = name.find(' ')

print('Seu Nome em Maiusculo é {}!'.format(n1))

print('Seu Nome em Minusculo é {}!'.format(n2))

print('Seu Nome ao Todo Tem {} Letras!'.format(len(name) - name.count(' ')))

print('Seu Primeiro Nome é {}!'.format(n4))
                  
      