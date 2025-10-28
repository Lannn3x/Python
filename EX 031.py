#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

#Python Exercise 031: Develop a program that asks for the distance of a trip in km.
#Calculate the ticket price, charging R$0.50 per km for trips up to 200 km and R$0.45 for longer trips.

n1 = float(input("Qual é a distancia da sua viagem? "))

print("voce esta prestes a correr {}KM!".format(n1))

v1 = n1 * 0.50

v2 = n1 * 0.45

if n1 <= 150:
    print("E o Preço Da Sua Passagem Sera R${:.2f} !".format(v1))

else:
    print("E o Preço Da Sua Passagem Sera R${:.2f} !".format(v2))

