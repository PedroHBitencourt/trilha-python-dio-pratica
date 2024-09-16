def sacar(valor):
    saldo = 500
    if saldo >= valor:
        saldo -= valor
        print("Saldo disponível: ", saldo)

sacar(100)