#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

#Python Exercise 034: Write a program that asks an employee for their salary and calculates the amount of their raise.
#For salaries above R$1250.00, calculate a 10% raise. For salaries below or equal to R$1250.00, the raise is 15%.

s = int(input("Qual É Seu Salario? "))

sm = s + (s * 15 / 100)

smm = s + (s * 10 /100)

if s<=1250:
    print("Quem Ganhava R${} Passou Ganhar R${:.2f}".format(s,sm))

else:
    print("Quem Ganhava R${} Passou Ganhar R${:.2f}".format(s,smm))