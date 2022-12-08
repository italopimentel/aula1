
def calculaSalario(valor_bruto):
    valor_pos_inss = valor_bruto - (valor_bruto*0.11)
    valor_pos_ir = valor_pos_inss - (valor_pos_inss*0.15)
    salario_liquido = valor_pos_ir

    return salario_liquido

salario_bruto = float(input("Digite o valor do seu salário bruto: "))
print("O seu salário líquido é de {} R$".format(calculaSalario(salario_bruto)))