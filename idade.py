
idade = int(input("Digite uma idade: "))
lista_idade = []
while idade >= 0:
    lista_idade.append(idade)
    idade = int(input("Digite uma idade: "))

contador = 0
soma_idade = 0

for i in lista_idade:
    soma_idade += i
    contador += 1

print("A média de idade foi: {}".format(soma_idade/contador))