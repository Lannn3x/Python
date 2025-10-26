#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

#Python Exercise 007: Develop a program that reads a student's two grades, calculates and displays their average.

num1 = float(input("Digite a primeira nota: "))

num2 = float(input("Digite a segunda nota: "))

num4 = (num1 + num2) / 2

print("a media do aluno é: {:.1f}".format(num4))