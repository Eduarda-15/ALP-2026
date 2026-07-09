def calculadora(num1,num2, operador):
    if operador == '+':
        return num1+num2
    elif operador == '-':
        return num1-num2
    elif operador == '*':
        return num1*num2
    elif operador == '/':
        return num1/num2
    else:
        return "Operador inválido!"

num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))
operador = input("Digite o operador: ")
print("Resultado:", calculadora(num1,num2, operador))
