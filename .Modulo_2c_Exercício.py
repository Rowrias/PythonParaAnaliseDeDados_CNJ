valor_base = 10.00

cond = True
while(cond):
    idade = int(input("Qual a sua idade? "))
    while(cond):
        if (idade < 5):
            print("Menores de 5 anos não pagam\nR$0,00")
            letra = input("aperte 's' para saber o preço através da sua idade ou aperte 'q' para sair: ")
            if (letra == 'q'):
                cond = False
                print("Tchau")
            if (letra == 's'):
                break
        elif (idade >= 5 and idade <= 12):
            print("Crianças entre 5 e 12 anos pagam meia-entrada\nR$", valor_base/2)
            letra = input("aperte 's' para saber o preço através da sua idade ou aperte 'q' para sair: ")
            if (letra == 'q'):
                cond = False
                print("Tchau")
            if (letra == 's'):
                break
        elif (idade >= 13 and idade <= 17):
            print("Crianças entre 13 e 17 anos têm 20% de desconto\nR$", valor_base-valor_base*0.2)
            letra = input("aperte 's' para saber o preço através da sua idade ou aperte 'q' para sair: ")
            if (letra == 'q'):
                cond = False
                print("Tchau")
            if (letra == 's'):
                break
        elif (idade >= 18 and idade <=70):
            print("Adultos entre 18 e 70 anos pagam o valor-base\n", valor_base)
            letra = input("aperte 's' para saber o preço através da sua idade ou aperte 'q' para sair: ")
            if (letra == 'q'):
                cond = False
                print("Tchau")
            if (letra == 's'):
                break           
        elif (idade > 70):
            print("Maiores de 70 anos não pagam\nR$0,00")
            letra = input("aperte 's' para saber o preço através da sua idade ou aperte 'q' para sair: ")
            if (letra == 'q'):
                cond = False
                print("Tchau")
            if (letra == 's'):
                break
