#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida

#Python Exercise 043: Develop a logic that reads a person's weight and height, calculates their Body Mass Index (BMI), and displays their status according to the table below:
#BMI below 18.5: Underweight
#Between 18.5 and 25: Ideal Weight
#25 to 30: Overweight
#30 to 40: Obesity
#Above 40: Morbid Obesity

kg = float(input("Digite Seu Peso Em KG: "))

alt = float(input("Digite Sua Algura Em M: "))

cal = kg / (alt * alt)

print("O IMC É De {:.2f}".format(cal))

if cal < 18.5:
    print("Abaixo Do Peso")

elif cal >= 18.5 and cal <= 25:
    print("Peso Ideal")

elif cal >= 25 and cal <=30:
    print("Sobrepeso")

elif cal >= 30 and cal <= 40:
    print("Obesidade")

elif cal >= 40:
    print("Obesidade Mórbida")