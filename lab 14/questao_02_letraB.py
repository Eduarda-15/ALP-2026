def ola(nome, sexualidade):
    if sexualidade == "neutro":
        return f"Olá {nome}, boas vindas!"
    elif sexualidade == "feminino":
        return f"Olá {nome}, seja bem vinda"
    elif sexualidade == "masculino":
        return f"Olá {nome}, seja bem vindo!"


print(ola("Leo", "neutro"))
print(ola("Mila", "feminino"))
print(ola("Alan", "masculino"))
