#abs() -> retorna o valor absoluto (módulo) de um número
#exemplo:
numero_negativo = -15
resultado = abs(numero_negativo)
print(resultado)

#filter() -> serve para extrair apenas os elementos de uma lista (ou outro iterável) que passam em um teste específico
#exemplo:
idades = [15, 18, 20, 12, 33, 16]
maiores = list(filter(lambda x: x >= 18, idades))
print(maiores)

#float() -> transforma textos ou números inteiros em números decimais (ponto flutuante).
#exemplo:
preco = float("15.50")
print(preco)

#input() -> serve para receber informações digitadas pelo usuário.
#exemplo:
nome = input("Digite o seu nome: ")
print("Bem vindo",nome,"!")

#int() -> converte um valor para um número inteiro.
#exemplo:
preco = 10.99
preco_inteiro = int(preco)
print(preco_inteiro)

#print() -> é usada para exibir informações quando o código roda.
#exemplo:
print("Olá, mundo!")

#range() -> cria uma lista de números em sequência, muito usada em laços de repetição.
#exemplo:
for numero in range(5):
    print(numero)

#str() -> serve para converter outros tipos de dados (números ou listas) em formato de texto (string).
#exemplo:
idade = 15
mensagem = "Eu tenho " + str(idade) + " anos."
print(mensagem)

#__import__() ->  é usada para carregar e importar módulos (arquivos de código) ou bibliotecas
# (conjunto de arquivos) para dentro do seu programa.
#exemplo:
import random
numero_dado = random.randint(1, 6)
print(numero_dado)

#round() -> serve para arredondar números.
#exemplo:
valor_1 = round(5.49)
print(valor_1)
