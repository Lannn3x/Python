#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

#Python Exercise 024: Create a program that reads the name of a city and says whether or not it starts with the name "SANTO".

c = str(input("Qual Cidade Você Nasceu? ")).strip()

m = c.upper()

e = 'SANTO' in m

print("{}".format(e))