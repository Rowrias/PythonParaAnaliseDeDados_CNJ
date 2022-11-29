#Manipulação de Strings e Arquivos
#Formatando Strings
anterior = 5000
atual = 5500
diferenca = atual - anterior
pct = diferenca/anterior * 100
frase = "A diferença de salário é de R${}, ou seja, {}%"
formatado = frase.format(diferenca, pct)
print(formatado)

salario = 7500
print("O seu salário é {}.".format(salario)) #formatando direto

salario = 7500
print("O seu salário é {:f}.".format(salario)) #imprimir como float
print("O seu salário é {:.2f}.".format(salario)) #imprimir como float 2 casas.

#Arquivos e Leitura

#Tipos de arquivo
#abrir e fechar arquivo
arq = open("00documento.txt", "r") #Para abrir um arquivo texto em modo leitura, use a função
arq.close() # É obrigatório que o arquivo seja fechado depois de usado.

#Read
arq = open("00documento.txt", "r")
conteudo = arq.read() # Lê o conteudo
print(conteudo)
arq.close()
#Readline
print("Readline")
arq = open("00documento.txt", "r")
conteudo = arq.readline()
while(conteudo != ""):
 print("Linha lida:", conteudo)
 conteudo = arq.readline()
arq.close()
#Iterando
print("Interando 1:")
arq = open("00documento.txt", "r")
for linha in arq:
 print("Linha lida:", linha)
arq.close()
#Iterando
print("Interando 2:")
arq = open("00documento.txt", "r")
for linha in arq:
 quebra = linha.split(" ")
 nome = quebra[0]
 idade = int(quebra[1])
 print(nome, "tem", idade, "anos de idade")
arq.close()

# Modo escrita (write)
f = open("documento.txt", "w") # se o arquivo existir sera substituído
# Modo anexagem (append)
f = open("documento.txt", "a") # o conteúdo é anexado no final do arquivo, caso já exista
# obrigatório fechar o arquivo
f.close()

# write() não adciona uma quebra de linha automaticamente no texto
#write() não aceita strings. Converta para string usando, por exemplo, str() o conteúdo a ser escrito quando necessário
#Exemplo
valor = 10
pi = 3.14
nome = "Maria da Silva"
arq = open("documento.txt", "w")
arq.write(str(valor))
arq.write(';')
arq.write(str(pi))
arq.write(';')
arq.write(nome)
arq.write('\n')
arq.close()
