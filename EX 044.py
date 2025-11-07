#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros

#Python Exercise 044: Develop a program that calculates the amount to be paid for a product, considering its regular price and payment terms:
#cash/check: 10% discount
#card: 5% discount
#up to 2 installments by card: regular price
#3 or more installments by card: 20% interest

print("====== LAN´S STORE ======")

preço = float(input("Digite O Preço Do Produto: R$ "))

print("""FORMAS DE PAGAMENTO
[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA NO CARTÃO
[ 3 ] 2x NO CARTÃO
[ 4 ] 3x OU MAIS NO CARTÃO""")

opção = int(input("Escolha A Opção De Pagamento: "))

if opção == 1:
    total = preço - (preço * 10 / 100)
    print("O Valor A Ser Pago É De R$ {:.2f} Com 10% De Desconto".format(total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print("O Valor A Ser Pago É De R$ {:.2f} Com 5% De Desconto".format(total))
elif opção == 3:
    total = preço
    parcela = total / 2
    print("O Valor A Ser Pago É De R$ {:.2f} Em 2x De R$ {:.2f} Sem Juros".format(total, parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input("Quantas Parcelas? "))
    parcela = total / totparc
    print("O Valor A Ser Pago É De R$ {:.2f} Em {}x De R$ {:.2f} Com Juros".format(total, totparc, parcela))
else:
    print("Opção Inválida De Pagamento. Tente Novamente!")