#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#Python Exercise 039: Write a program that reads a young person's birth year and informs them,
# according to their age, whether they still need to register for military service,
# whether it is the exact time to register, or whether the registration period has already passed. 
# Your program should also show the time remaining or that has passed since the deadline.

from datetime import date

data = date.today().year

print("SEJA BEM VINDO AO ALISTAMENTO MILITAR !")

ano = int(input("Ano De Nacimento: "))


idade = data - ano

print("Quem Nasceu Em {} tem {} Anos Em {}".format(ano,idade,data))

if idade == 18:
    print("Você Tem Que Se Alistar IMEDIATAMENTE")

elif idade > 18:
    maior = idade - 18
    antes = data - maior
    print("Você Já Deveria Ter Alistado Há {} Anos.".format(maior))
    print("Você Se Alistou Em {}".format(antes))

elif idade < 18:
    menor = 18 - idade
    atual = menor + data
    print("Você Ainda Faltão {} Anos Para Você Se Alistar".format(menor))
    print("Seu Alistamento Será Em {}".format(atual))