#Erros: Uma variável indefinida, (soma), no início do programa.
#Faltava a função dela de terminar com a linha do código,fazendo ele parar.
maior = float('-inf')
soma = 0
while soma < 10:
    num = int(input("Digite um número: "))
    if num > maior:
       maior = num
    soma += 1
print('O maior número é', maior)
