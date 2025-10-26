#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

#Python Exercise 011: Write a program that reads the width and height of a wall in meters, calculates its area, and the amount of paint needed to paint it,
#knowing that each liter of paint paints an area of ​​2 square meters.

n1 = float(input("Largura Da Parede: "))

n2 = float(input("Altura Da Parede: "))

c1 = (n1 * n2)

c2 = (c1 / 10)

print("Sua Parede Tem A Dimenção De {}x{} E Sua Area É De {}M².".format(n1,n2,c1))
print("Para Pintar Essa Parede, Sera Preciso De {}L De Tinta".format(c2))