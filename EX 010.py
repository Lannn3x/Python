#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

#Python Exercise 010: Create a program that reads how much money a person has in their wallet and shows how many dollars they can buy.

n1 = float(input("Digite Um Valor De Dinheiro Para Converter Para US$: "))

n2 = (n1 / 5.39)

print("O Dinheiro Convertido Voce Tem US$ {:.2} ".format(n2))