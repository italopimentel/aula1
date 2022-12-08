
def validar_tempo(tempo):
        inicial_array = tempo
        while (int(inicial_array[0]) > 23 or int(inicial_array[0]) < 0) or (int(inicial_array[1]) > 59 or int(inicial_array[1]) < 0):
            print("valor inválido!")
            tempo_inicial = input("Digite a hora inicial: ")
            inicial_array = tempo_inicial.split(":")
        return inicial_array

tempo_inicial = validar_tempo(input("Digite a hora inicial: "))
print(tempo_inicial)

