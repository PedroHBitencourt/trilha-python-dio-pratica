nome = "Pedro"
idade = 24
profissao = "Programador"
linguagem = "Python"

#MÉTODO FORMAT
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.". format(nome, idade, profissao, linguagem))
#VANTAGENS DO MÉTODO FORMAT
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.". format(linguagem, profissao, idade, nome))

#MÉTODO F-STRING
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")