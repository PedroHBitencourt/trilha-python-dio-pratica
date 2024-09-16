texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print()


for numero in range (0, 11):
    print(numero, end=", ")
else:
    print(" ")

#Exibindo tabuada do 5
for numero in range (0, 51, 5):
    print(numero, end=", ")
else:
    print(" ")