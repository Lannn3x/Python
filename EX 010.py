#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

n1 = float(input("Digite Um Valor De Dinheiro Para Converter Para US$: "))

n2 = (n1 / 5.39)

print("O Dinheiro Convertido Voce Tem US$ {:.2} ".format(n2))