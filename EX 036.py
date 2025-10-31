#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#Python Exercise 036: Write a program to approve a bank loan for the purchase of a house.
#Ask for the value of the house, the buyer's salary, and how many years they will pay it off.
#The monthly payment cannot exceed 30% of the salary, otherwise the loan will be denied.

c = float(input('Valor Da Casa: '))

s = float(input("Salario Do Comprador: "))

f = int(input("Quantos Anos De Financiamento? "))

pre = c / (f * 12)

m = s * 30 / 100

print("Para Pagar Uma Casa De R${:.2f} Em {} Anos A Prestação Será De R${:.2f} ".format(c,f,pre))

if pre >= m :
    print("\033[31m EMPRESTIMO NEGADO!\033[m")

else :
    print("\033[32m EMPRESTIMO PERMITIDO!\033[m")