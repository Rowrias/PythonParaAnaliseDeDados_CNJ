# Modulo 3c
#Importando
import Modulo_3cMatematica

valor = int(input("Digite um valor ou -1 para sair: "))
while(valor != -1):
    resultado = Modulo_3cMatematica.fatorial(valor)
if (resultado != -1):
 print("O fatorial de", valor, "é", resultado)
else:
 print("Impossível calcular o fatorial de", valor)
valor = int(input("Digite um valor ou -1 para sair: "))
