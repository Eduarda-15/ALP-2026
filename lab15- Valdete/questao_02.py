def transformacao(celsius):
    conta = (celsius*1.8)+32
    return conta
celsius = int(input("Digite o Graus Celsius: "))
f = transformacao(celsius)
print(f"A transformação de Graus celsius para Fahrenheit é: {f}")
