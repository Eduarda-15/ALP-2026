def soma_digitos(num):
    soma = 0
    while num >0:
        digito = num % 10
        soma += digito
        num = num //10
    return soma
num = int(input("Digite um número: "))
resul = soma_digitos(num)
print("A soma dos dígitos é:", resul)
