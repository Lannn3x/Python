#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

num1 = float(input("Digite a primeira nota: "))

num2 = float(input("Digite a segunda nota: "))

num4 = (num1 + num2) / 2

print("a media do aluno é: {:.1f}".format(num4))

if num4 < 5:
  print("O Aluno Esta Reprovado!")

elif 7 > num4 >= 5:
  print("O Aluno Esta De Recuperação!")

elif num4 > 7:
  print("O Aluno Foi Aprovado")