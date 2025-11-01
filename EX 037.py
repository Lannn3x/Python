#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
#para binário, 2 para octal e 3 para hexadecimal.

#Python Exercise 037: Write a Python program that reads any integer and asks the user to choose the conversion base: #for binary, 2 for octal, and 3 for hexadecimal.

n = int(input("Digite Um Numero Inteiro: "))

print("""Escolha Uma Opção: 
[1] BINARIO
[2] OCTAL 
[3] HEXADECIMAL:  """)

op = int(input("Qual Operação Você Escolhe? "))

if op == 1:
    print("{} Convertido Para \033[32m BINARIO \033[m é {}".format(n,bin(n) [2:]))

elif op == 2:
    print("{} Convertido Para \033[32m OCTAL \033[m é {}".format(n, oct(n) [2:]))

elif op == 3:
    print("{} Convertido Para \033[32m HEXADECIMAL \033[m é {}".format(n, hex(n) [2:]))

else:
    print("\033[31m OPERAÇÃO INVALIDA \033[m")