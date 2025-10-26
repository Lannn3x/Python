#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#Python Exercise 015: Write a program that queries the number of kilometers traveled by a rental car and the number of days it was rented. 
#Calculate the price, knowing that the car costs R$60 per day and R$0.15 per kilometer driven.

d = int(input("Quantos Dias Alugados? "))

km = float(input("Quantos Km Rodados? "))

c1 = (60 * d)+(0.15 * km)


print("O total A Pagar é De R%{}!".format(c1))