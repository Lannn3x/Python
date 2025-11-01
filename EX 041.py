#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER

#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MESTRE

from datetime import date

hoje = date.today().year

ano = int(input("Que Ano Você Nasceu? "))

data = (hoje - ano)

print("Você Nasceu Em {} E Tem {} Anos".format(ano,data))

if data < 9:
    print("Classificação: Mirim")

elif data >= 9 and data <= 14:
    print("Classificação: Infantil")

elif data >= 14 and data <= 19:
    print("Classificação>: Júnior")

elif data >= 19 and data <= 25:
    print("Classificação: Sênior")

elif data >= 25:
    print("Classificação: Master")