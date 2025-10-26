#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

#Python Exercise 008: Write a program that reads a value in meters and displays it converted to centimeters and millimeters.

n1 = float(input('digite um valor em metros:'))

n2=n1*100
n3=n1*1000 

print("O seu valor em metros é {},\n e em centimetro é {}\n".format(n2,n3))