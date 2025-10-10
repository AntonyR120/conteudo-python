valor_hora = float(input("Quando você ganha por hora?: "))
valor_mes = float(input("Quantas horas você trabalhou no mês: "))
salario_bruto = valor_hora * valor_mes
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato
print("Salário Bruto: R$", salario_bruto)
print("Desconto INSS: R$",desconto_inss)
print("Desconto IR: R$",desconto_ir)
print("Salário Líquido: R$",salario_liquido)