#Erro: faltava acresentar uma variável que controlasse a quantidade de números á serem digitados (cont)
#Faltou um print que informasse o resultado da soma
soma = 0
cont = 0
while cont <= 9:
    num = int(input("Digite um número para somar: "))
    soma += num
    cont += 1
print("A soma dos 10 números digitados dá:", soma)

