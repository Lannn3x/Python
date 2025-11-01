#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

#Python Exercise 038: Write a program that reads two integers and compares them, displaying the following message on the screen:
#The first value is greater
#The second value is greater
#There is no greater value, they are both equal

n = int(input('Primeiro Valor: '))

n2 = int(input("Segundo Valor: "))

if n > n2:
    print("O Primeiro Valor É Maior !")

elif n2 > n:
    print("O Segundo Valor É Maior !")
elif n == n2:
    print("Não Existe Valor Maior, Os Dois Valor São Iguais !")
