#Modulo 2

carro1 = "Honda"
carro2 = "Toyota"
print(carro1 == carro2)
carro1 = "Honda"
carro2 = "honda"
print(carro1.lower() == carro2)

# Comando "if"
carro = "suzuki"
if (carro.title() == "Suzuki"):
    print("Acertou!")

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Pode dirigir no Brasil...")
if idade < 18:
    print("Não pode dirigir no Brasil!")
if idade >15:
    print("Pode dirigir nos EUA...")
if idade >= 16 and idade < 21:
    print("Pode dirigir, mas não comprar álcool nos EUA")

# "or" , "and"
pessoa1 = 27 ; pessoa2 = 25 ; papel1 = 'responsável' ; papel2 = "responsável"

if ((pessoa1 >= 18) or (pessoa2 >= 18)) and ((papel1 == "responsável") or (papel2 == "responsável")):
    print("Menor pode entrar no cinema acompanhado por pais ou tutor")

if ((pessoa1 >= 18) or (pessoa2 >= 18)) and ((papel1 == "responsável") or (papel2 == "responsável")) and not ((pessoa1 < 12) or (pessoa2 < 12)):
    print("Ambos assistem o filme no cinema...")


# if Condicionais
idade = int(input("Digite sua idade: "))
if (idade > 16 or idade >=70):
    print("Pode votar!")
    print("Já fez seu título de eleitor?")
if (idade >= 18 and idade <70):
    print("Na sua idade, o voto é obrigatório.")
if (idade < 16):
    print("Você ainda não pode votar")

#if - else
idade = int(input("Digite sua idade: "))
if (idade >= 16):
    print("Você pode votar!")
else:
    print("Você ainda não pode votar!")

# if - elif - else
a = int(input("Digite valor de 'A': "))
b = int(input("Digite valor de 'B': "))
if (a > b):
    print("A é maior do que B ({} > {})".format(a,b))
elif (a < b):
    print("B é maior do que A ({} > {})".format(b,a))
else:
    print("A e B são iguais!")

# cadeia if - elif - else
opcao = input("Forma de pagamento [c|d|b|o]: ")
if (opcao == 'c'):
    print("Pagamento no crédito sem desconto.")
elif (opcao == 'd'):
    print("Pagamento no débito com 3% de desconto.")
elif (opcao == 'b'):
    print("Pagamento no boleto com 5% de desconto.")
elif (opcao == 'o'):
    print("Pagamento em dinheiro com 10% de desconto.")
else:
    print("Opção '{}' não cadastrada".format(opcao))

#if - else - else
idade = int(input("Digite sua idade: "))
if (idade >= 16):
    print("Você já pode votar se tiver título de eleitor.")
    if (idade >= 18 and idade <= 70):
        print("Se você é alfabetizado, seu voto é obrigatório!")
    else:
        print("Seu voto é facultativo.")
else:
    print("Você ainda não pode votar...")
