#Manipulação de Strings e Arquivos

#Strings
print("Strings:")
nome = "Maria Silva"
frase = "Curso de Python"
print("Num caracs", len(frase)) # conta os espaços
linguagem = frase[9:len(frase)] # nove em diante
print(linguagem)
print("Primeira Letra;", frase[0])

#Replace
print("Replace:") 
frase = "Esse é o curso de linguagem C++. Você pode criar programas em C++."
mudanca = frase.replace("C++", "Python")
somente_prim = frase.replace("C++", "Python", 1) 
print(frase) # original
print(mudanca) # faz a mudança e a frase original continua
print(somente_prim) # especifica o número limite de substituiçoes

#Concatenando
print("Concatenando:")
nome_curso = "Python"
ola = "Bom dia."
frase = ola + " Esse é o curso de " + nome_curso + "."
print(frase)

#Caracteres de controle
#"\n" insere uma quebra de linha
#"\t" insere uma tabulação
frase = "Esse é um texto\nde\texemplo"
print(frase)

#Caixa
print("Caixa:")
#Maiúsculo usando: upper()
#Minúsculo usando: lower()
#Primeira maiúscula e demais minúsculas: capitalize()
frase1 = "CURSO de Python"
print(frase1.upper())
print(frase1.lower())
print(frase1.capitalize())

#Split
#Utilize split(string_de_quebra) para “quebrar” uma 
#string em uma lista de strings.
frase = "Esse é o curso de Python - Foco em iniciantes"
print("Split da lista 1:")
lista1 = frase.split(" ") # separa quando houver espaço
for item in lista1:
    print(item)
print("Split da lista 2:")
lista2 = frase.split("-") # separa quando houver hifem
for item in lista2:
    print(item)

#Índice
#Para encontrar o índice de uma palavra ou caractere, use a função find()
print("Índice:")
frase = "Olá mundo teste isso vai ficar teste final"
inicio = frase.find("teste") + len("teste")
fim = frase.find("teste", inicio)
print(frase[inicio:fim])

#lista de Funções:
#   count()        Quantas vezes a palavra aparece
#   endswith()     Verifica se a string termina com determinada palavra
#   startswith()   Verifica se a string começa com determinada palavra
#   islower()      Verifica se todos caracteres estão em caixa baixa
#   isnumeric()    Verifica se todos caracteres são numéricos
#   isspace()      Verifica se todos os caracteres são espaços em branco
#   strip()        Remove caracteres em branco do começo da string
#   isascii()      Verifica se todos os caracteres são ASCII

