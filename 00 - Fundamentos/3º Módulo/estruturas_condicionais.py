MAIOR_IDADE = 18
IDADE_ESPECIAL = 12
idade = int(input("Qual a sua idade? "))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, você já pode tirar sua CNH")
elif idade == IDADE_ESPECIAL:
    print("você pode fazer aulas teóricas, mas não pode fazer aulas práticas")
else:
    print("Você é menor de idade, você não pode tirar sua CNH")