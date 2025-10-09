import math
tamanho = float(input("Digite o tamanho em metros quadrados: "))
litros_por_metro= 1 / 3
capacidade_lata = 18
preco_lata = 80.00
litros_nescessarios = tamanho * litros_por_metro
latas_nescessarias = math.ceil(litros_nescessarios / capacidade_lata)
preco_total = latas_nescessarias * preco_lata
print("Você precisará de", latas_nescessarias,"lata(s) de tinta")
print("O custo total será de R$",preco_total)