#*args permite que você passe uma quantidade variável de argumentos posicionais para uma função. Ele os recebe como uma tupla.
def soma(*args):
    return sum(args)

print(soma(1, 2, 3))  # Saída: 6
print(soma(4, 5, 6, 7, 8))  # Saída: 30

#**kwargs permite que você passe uma quantidade variável de argumentos nomeados (chave-valor) para uma função. Ele os recebe como um dicionário.
def exibir_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

exibir_informacoes(nome="Ana", idade=25, cidade="São Paulo")

#Você pode usar ambos em uma função, e geralmente os *args vêm antes de **kwargs.

def misturar_args_kwargs(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)

misturar_args_kwargs(1, 2, 3, nome="Pedro", idade=30)