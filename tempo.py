
lista_hora = []
lista_minuto = []

#falta terminar e tratar possíveis resultados 

while True:
    num = int(input("Digite a hora inicial: "))
    if num >= 1 and num <= 23:
         lista_hora.append(num)
         break
    else:
        print("valor inválido, digite novamente")

while True:
    num = int(input("Digite o minuto inicial: "))
    if num >= 1 and num <= 59:
        lista_minuto.append(num)
        break
    else:
        print("valor inválido, digite novamente")

while True:
    num = int(input("Digite a hora final: "))
    if (num >= 1 and num <= 23):
         lista_hora.append(num)
         break
    else:
        print("valor inválido, digite novamente")

while True:
    num = int(input("Digite o minuto final: "))
    if num >= 1 and num <= 59:
        lista_minuto.append(num)
        break
    else:
        print("valor inválido, digite novamente")

print ("o jogo durou {} horas e {} minutos".format(lista_hora[1] - lista_hora[0], lista_minuto[1] - lista_minuto[0]))