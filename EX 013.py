#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

n1 = float(input("Qual O Salario Do Funcionario? $"))

c1 = n1 + (n1 * 15 / 100)

print("Um Funcionario Que Ganhava R%{}, Com 15% De Aumento, Passar a Receber R%{}".format(n1,c1))