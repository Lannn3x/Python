#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

#Python Exercise 045: Create a program that makes the computer play Rock-Paper-Scissors with you.

import random 

itens = ("Pedra", "Papel", "Tesoura")

computador = random.randint(0, 2)

print("""Suas Opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA""")

jogador = int(input("Qual é A Sua Jogada? "))

print("Computador Jogou {}".format(itens[computador]))
print("Jogador Jogou {}".format(itens[jogador]))

if computador == 0: 
    if jogador == 1:
        print("Jogador Vence")
    elif jogador == 2:
        print("Computador Vence")
    else:
        print("Jogada Inválida!")  
elif computador == 1: 
    if jogador == 2:
        print("Jogador Vence")
    elif jogador == 0:
        print("Computador Vence")
    else:
        print("Jogada Inválida!")
elif computador == 2:
    if jogador == 0:
        print("Jogador Vence")
    elif jogador == 1:
        print("Computador Vence")
    else:
        print("Jogada Inválida!")