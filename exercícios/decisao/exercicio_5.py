numero1 = int(input("Digite sua primeira nota: "))
numero2 = int(input("Digite o segunda notas: "))
notas = (numero1 + numero2) / 2
print("Sua média é",notas)
if notas == 10:
    print("Parebéns, você passou de ano e é um aluno(a) de destaque!")
elif notas >= 7:
    print("Parabéns, você passou de ano")
else:
    print("Você está reprovado")