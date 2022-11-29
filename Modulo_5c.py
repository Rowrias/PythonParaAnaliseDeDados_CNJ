# #Manipulação de Strings e Arquivos
# Arquivos Delimitados

# CSV - comma-separated values. Tipos de arquivo de texto delimitado, Os valores são separados por vígula
# Exemplo de CSV
#Nome;Idade;Salário
#Maria Silva;45;8500,85
#José Oliveira;30;5500,4
#Marcos Santos;35;8000

#Lendo um CSV
arq = open("00exemplo.csv", "r")
arq.readline() #descartando primeira linha
idades = 0
salarios = 0
qtde = 0
for linha in arq:
 quebra = linha.split(';')
 idades = idades + int(quebra[1])
 salarios = salarios + float(quebra[2].replace(',','.'))
 qtde = qtde + 1
arq.close()
print("A idade media é", idades/qtde)
print("O salário médio é", salarios/qtde)

# Biblioteca padrão para CSVs
# O Python conta com uma biblioteca padrão para leitura de CSVs

import csv
arq = open("00exemplo.csv", "r")
csv_reader = csv.reader(arq, delimiter = ';')
next(csv_reader) #pular a primeira linha
idades = 0
salarios = 0
qtde = 0
for linha in csv_reader:
 idades = idades + int(linha[1])
 salarios = salarios + float(linha[2].replace(',','.'))
 qtde = qtde + 1
arq.close()
print("A idade media é", idades/qtde)
print("O salário médio é", salarios/qtde)
