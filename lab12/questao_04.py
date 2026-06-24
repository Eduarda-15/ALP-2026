num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num_casas_decimais = 2
valor_absoluto = abs(num1 - num2)
valor_arredondado = round(valor_absoluto ,num_casas_decimais)
print("A diferença absoluta entre os números é: ",valor_arredondado )
