valor = int(input("Digite o valor: "))
contador = valor
resultado = 1
while contador > 0:
    resultado = resultado * contador
    contador = contador - 1
print(f"O fatorial de {valor} é {resultado}")
def fatorial(valor):
    if(valor == 1):
        return 1
    return fatorial (valor - 1) * valor