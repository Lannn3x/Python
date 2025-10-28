#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

#Python Exercise 027: Write a program that reads a person's full name, then displays the first and last name separately.

n = str(input("Qual é Seu Nome? ")).strip()

p = n.split()

print("QUE NOME LINDO !")

print('Seu Primeiro Nome é {}'.format(p[0]))

print("E Seu Ultimo Nome é {}".format(p[len(p)-1]))