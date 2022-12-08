
lista_idade = []
idade = int(input("Digite uma idade: "))
try:
    while idade >= 0:
        lista_idade.append(idade)
        idade = int(input("Digite uma idade: "))

    soma_idade = 0

    for valor in lista_idade:
        soma_idade += valor

    print("A média de idade foi: {}".format(soma_idade/len(lista_idade)))
except ZeroDivisionError:
    print("O programa foi encerrado pois não foi digitado nenhum valor válido")