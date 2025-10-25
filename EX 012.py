#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

n1 = float(input("Digite O Valor Do Produto? $:"))

c1 = n1 - (n1 * 5 / 100)

print("O Valor Do Produto Que Custa {}, Com Desconto De 5% Ficará {}".format(n1,c1))