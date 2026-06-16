while True:
    perg = input("Você quer saber como manter uma pessoa ingênua ocupada por horas? S/N > ")
    if perg == "SIM" or perg == "S" or perg == "s" or perg == "sim":
        continue
    elif perg == "NÃO" or perg == "N" or perg == "n" or perg == "não":
        print("Obrigada tenha um bom dia!:)")
        break
    else:
        print("não é uma resposta válida de sim/não.")
        continue
