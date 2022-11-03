#Modulo 2

#Repetição (Iteração) - 'for"
for x in range(3):
    print(x)

palavra = "Python"
n = len(palavra)
for x in range(n):
    print(x)

palavra = "Python"
for y in range(len(palavra)):
    print(palavra)

palavra = "Python"
for x in palavra:
    print(x)

#Comando While

n = int(input("Digite um número inteiro: "))
while (n > 0):
    print(n)
    n -= 1 #equivalente a n = n - 1
print("Tempo esgotado!")

while(True):
    letra = input("Digite uma letra diferente de 'q':  ")
    if (letra == "q"):
        break
    print("Você digitou a letra 'q' !!!")

cond = True
while(cond):
    opção = input("Digite 'sair' para terminar o laço")
    if opção == 'sair':
        cond = False
    else:
        print("Ainda no laço...")
