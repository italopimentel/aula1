num = 0
quant_par = 0

for i in range(0,5):
    num = (int(input("digite um valor impar ou par: ")))
    if num % 2 == 0:
        quant_par += 1 

print("a quantidade de numeros pares é:{} ".format(quant_par))
