import math

area =float(input("Informe área a ser pintada: "))
cob_por_metro = 3
qtd_tinta_lata = 18
valor_lata = 80.0

litros_nescessarios = area / cob_por_metro
print("São nescessários",litros_nescessarios,"L de tinta")
qtd_latas = litros_nescessarios /qtd_tinta_lata

print("### Com o valor exato ###")
valor = qtd_latas * valor_lata
print("O valor nescessário da tinta é: R$",round(valor,2))

print("### Com quantidades inteiras de latas ###")
qtd_latas = math.ceil(qtd_latas)
print("São nescessários",qtd_latas,"latas de tinta")
valor = qtd_latas * valor_lata
print("O valor nescessário de tinta, é R$",valor)