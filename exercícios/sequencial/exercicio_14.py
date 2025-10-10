limte_peso = 50
multa_por_kg = 4
peso_peixe = float(input("Informe o peso total: "))
if peso_peixe > limte_peso:
  excedente = peso_peixe - limte_peso
  multa = excedente * multa_por_kg
  print("Houveram",excedente,"kg de peixe a mais do permitido")
  print("O valor de multa é R$",multa)
else:
    print("Não foi maior do que o permitido")