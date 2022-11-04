# Exemplo para exportar para o modulo 3c

def fatorial(n):
    if (n < 0):
        return -1 #retornando -1 para indicar um erro
    res = 1
    while(n > 1):
        res = res*n
        n = n -1
    return res
valor = int(input("Digite um valor ou -1 para sair: "))
while(valor != -1):
    resultado = fatorial(valor)
    if (resultado != -1):
            print("O fatorial de", valor, "é", resultado)
    else:
            print("Impossível calcular o fatorial de", valor)
    valor = int(input("Digite um valor ou -1 para sair: "))

