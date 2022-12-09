def valorPagamento(valor_prestacao, dias_atrasados):
    valor_a_ser_pago = 0 

    if dias_atrasados <= 0:
        valor_a_ser_pago = valor_prestacao
    else:
        multa = valor_prestacao + (valor_prestacao*0.03)
        juros = (valor_prestacao*(1 + 0.001)**dias_atrasados) - valor_prestacao
        valor_a_ser_pago = round(multa + juros, 1)
    return valor_a_ser_pago

prestacao = 1
atraso = 0
valor_total = 0
quant_pagas = 0

while prestacao != 0:
    prestacao = float(input("Digite o valor da prestação: "))
    if prestacao == 0:
        break
    atraso = int(input("Digite a quantidade de dias atrasados: "))
    valor_pago = valorPagamento(prestacao, atraso)
    print("\nO valor a ser pago é: {} R$\n".format(valor_pago))
    valor_total += valor_pago
    quant_pagas += 1

print("\n")
print("A valor total das prestações pagas hoje foi: {} R$".format(valor_total))
print("A quantidade total de prestações pagas hoje foi: {}".format(quant_pagas))




    