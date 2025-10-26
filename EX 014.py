#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input("Informe A Temperatura Em °C: "))

f= (1.8 * c) + 32

print("A temperatura de {}°C Corresponde A {}°F".format(c,f))