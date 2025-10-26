#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#Python Exercise 006: Create an algorithm that reads a number and displays its double, triple, and square root.

num = int(input("Digite um número: "))

print("o dobro de {} é {}".format(num, (num*2)))

print("o triplo de {} é {}".format(num, (num*3)))

print("a raiz quadrada de {} é {:.2f}".format(num, (num**(1/2))))