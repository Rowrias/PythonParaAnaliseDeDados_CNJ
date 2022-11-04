#Modulo 3b

#Lista são heterogêneas
lista_inteiros = [1,2,3]
elementos = ["casa", 1, "banana", lista_inteiros]
for item in elementos:
    print(item, type(item))

#Arrays (Vetores)
#Python provê arrays (vetores) homogêneos
#Operam de maneira similar a lista mas em um array, todos 
#elementos precisam ser do mesmo tipo
#(Muito) Mais eficiente do ponto de vista computacional
#Veja mais sobre arrays em docs.python.org/3/library/array.html

# 3 - Tuplas "()" - São imutáveis, similar a lista
tupla_compras = ("maçãs", "leite", "arroz", "frango", "trigo")
print(tupla_compras)
print("O item 1 é", tupla_compras[1])
#tupla_compras[0] = "tomate" TypeError: 'tuple' object does not support item assignment Você não pode modificar uma tupla!

import sys
lista = ["maçãs", "leite", "arroz", "frango", "trigo"]
tupla = ("maçãs", "leite", "arroz", "frango", "trigo")
print("Tamanho na memória da tupla:", sys.getsizeof(tupla))
print("Tamanho na memória da lista:", sys.getsizeof(lista))

# 4 - Funções
def saudacao(): #Cria a função
    print("Ola, bem vindo.")
    print("Esse é o curso de Python.")
saudacao()      #Chama a função
# Exemplo
def saudacao(nome, periodo):
    if (periodo == 'm'):
        print("Bom dia,", nome + '.')
    elif(periodo == 't'):
        print("Boa tarde,", nome + '.')
    elif(periodo == 'n'):
        print("Boa noite,", nome + '.')
    else:
        print("Ops, período inválido.")
        print("Esse é o curso de Python.")

saudacao("Paulo", 'n')

# Valor default
def saudacao(nome, periodo = 'm'): # periodo = 'm'
    if (periodo == 'm'):
        print("Bom dia,", nome + '.', "Essa é a saudação padrão.")
    elif(periodo == 't'):
        print("Boa tarde,", nome + '.')
    elif(periodo == 'n'):
        print("Boa noite,", nome + '.')
    else:
        print("Ops, período inválido.")
        print("Esse é o curso de Python.")

saudacao("Paulo")

# 5 - Retorno e boas práticas
# Fatorial
# A função fatorial imprime o resultado. 
# Isso (geralmente) é uma má prática. Idealmente, essa função deveria 
#retornar (devolver) o resultado da conta.
#Quem chamou a função decide o que fazer com esse resultado.

def fatorial(n1):
    res = 1
    while(n1 > 1):
        res = res*n1
        n1 = n1 -1
    print("O fatorial é", res)

valor = int(input("Ex1: Digite um valor ou -1 para sair: "))
while(valor != -1):
    fatorial(valor)
    valor = int(input("Ex1: Digite um valor ou -1 para sair: "))

# Fatorial melhorado
def fatorial(n2):
    if (n2 < 0):
        return -1 #retornando -1 para indicar um erro
    res = 1
    while(n2 > 1):
        res = res*n2
        n2 = n2 -1
    return res

valor = int(input("Ex2: Digite um valor ou -1 para sair: "))
while(valor != -1):
    resultado = fatorial(valor)
    if (resultado != -1):
        print("O fatorial de", valor, "é", resultado)
    else:
        print("Impossível calcular o fatorial de", valor)
    valor = int(input("Ex2: Digite um valor ou -1 para sair: "))
