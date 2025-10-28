#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

#Python Exercise 029: Write a program that reads a car's speed.
#If it exceeds 80 km/h, display a message saying it has been fined. The fine will cost R$7.00 for each km over the limit.

v = float(input("Qual é A velocidade do carro? "))

c = (v - 80) * 7

if v <=80 :
    print("Esta tudo certo, tenha um bom dia!")

else:
    print("MULTADO, Voce passou o limite permitido de 80KM/h!")
    print("Voce terar que pagar R${:.2f} de Multa!".format(c))