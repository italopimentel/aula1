hora_ini_valida = False

while hora_ini_valida == False:
    #cria um array separando a hora dos minutos ----- hora-> elemento 0 do array --- minuto-> elemento 1 do array
    horario = input("Digite a hora e os minutos iniciais sepados por ':' ").split(":")
    #verifica se o horário digitado é válido
    if (int(horario[0]) < 24 and int(horario[0]) >= 0) and (int(horario[1]) < 60 and int(horario[1]) >= 0):
        hora_ini_valida = True
    else:
        print("Hora inválida, digite novamente!")

#transforma o array de string em array de inteiro
horario_inicial = [int(horario[0]), int(horario[1])]

#---------------------------------------------------------------------------------------------------------------------------------------------------
hora_fin_valida = False

while hora_fin_valida == False:
    #cria um array separando a hora dos minutos ----- hora-> elemento 0 do array --- minuto-> elemento 1 do array
    horario = input("Digite a hora e os minutos finais sepados por ':' ").split(":")
    #verifica se o horário digitado é válido
    if (int(horario[0]) < 24 and int(horario[0]) >= 0) and (int(horario[1]) < 60 and int(horario[1]) >= 0):
        hora_fin_valida = True
    else:
        print("Hora inválida, digite novamente corretamente!")
    
horario_final = [int(horario[0]), int(horario[1])] 

#condição caso a hora final seja menor do que a inicial
if horario_final[0] < horario_inicial[0]:
    resultado_hora = (horario_final[0] + 24) - horario_inicial[0]
else:
   resultado_hora = horario_final[0] - horario_inicial[0]

#condição caso o minuto final seja menor do que o inicial
if horario_final[1] < horario_inicial[1]:
    resultado_minuto = (horario_final[1] - horario_inicial[1]) + 60
    resultado_hora -= 1
else:
    resultado_minuto = horario_final[1] - horario_inicial[1]

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(resultado_hora,resultado_minuto))