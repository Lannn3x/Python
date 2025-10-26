#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

#Python Exercise 004: Write a program that reads something from the keyboard and displays its primitive type and all possible information about it on the screen.

algo = input("Digite algo: ")
print("O tipo primitivo desse valor é:", type(algo))

espaco = algo.isspace()
print("Só tem espaços?", espaco)

numero = algo.isnumeric()
print("É um número?", numero)

alfanumerico = algo.isalnum()
print("É alfanumerico?", alfanumerico)

alfabetico = algo.isalpha()
print("É alfabetico?", alfabetico)

maiúsculas = algo.isupper()
print("Está em maiúsculas?", algo.isupper())

minusculas = algo.islower()
print("Está em minusculas?", algo.islower())

capitalizada = algo.istitle()
print("Está capitalizada?", algo.istitle())