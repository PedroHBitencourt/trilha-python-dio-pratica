conta_normal = False
conta_universitaria = True
conta_especial = True

saldo = 2000
saque = 2200
cheque_especial = 450

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saque + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")

elif conta_especial:
    print("Conta especial selecionada!")

else:
    print("")