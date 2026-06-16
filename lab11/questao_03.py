while True:
    import time
    import random
    prob = random.randint(1, 10)
    if prob <=5:
        resposta='SIM'
    else:
        resposta='NÃO'
    perg = input("Deseja fazer uma pergunta? > ")
    if perg == "NÃO" or perg == "N" or perg == "n" or perg == "não":
        print("Tudo bem!! :)")
        break
    if perg == "SIM" or perg == "S" or perg == "s" or perg == "sim":
        ler = input("Qual a pergunta?")
        print("Espere um segundo...")
        time.sleep(2)
        print("Consultando o universo...")
        time.sleep(2)
        print("Quase lá!!!")
        time.sleep(2)
        print("TENHO A RESPOSTA!!")
        time.sleep(2)
        print(resposta)
