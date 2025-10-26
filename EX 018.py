#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

#Python Exercise 018: Write a program that reads any angle and displays on the screen the value of the sine, cosine and tangent of that angle.

import math

n1 = float(input("Digite um angulo Qualquer: "))

c1 = math.cos(math.radians (n1))

c2 = math.sin(math.radians (n1))

c3 = math.tan(math.radians (n1))

print("O Ângulo De {} Tem O CONSSENO De {:.2f}".format(n1,c1))

print("O Ângulo De {} Tem O SENO De {:.2f}".format(n1,c2))

print("O Ângulo De {} Tem A TANGENTE De {:.2f}".format(n1,c3))