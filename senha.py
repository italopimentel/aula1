acesso_permitido = False

while acesso_permitido == False:
    senha = input("Digite uma senha: ")
    if senha == '2002':
        acesso_permitido = True
    else:
        print("Acesso negado!")
    
print("Acesso permitido!")