nome = input("Digite o seu nome: ")
while len(nome) < 3:
    print("Nome inválido, ele precisa ter mais de 3 caracteres")
    nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
while idade < 0 or idade > 150:
    print("Idade inválida, ela precisa ser entre 0 e 150")
    idade = int(input("Digite a sua idade: "))
salario = float(input("Digite seu salário: "))
while salario <0:
    print("Salário inválido, ele precisa ser maior que 0")
    salario = float(input("Digite seu salário: "))
estado_civil = input("Digite o código do seu estado civil: ")
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and  estado_civil!='d':
    print("Código inválido, digite 's' ´para solteiro,'c' para casado, 'v' para viúvo ou 'd' para divorciado ")
    estado_civil = input("Digite o código do seu estado civil: ")

print("Dados registrados")
print("Nome:",nome)
print("Idade:",idade,"anos")
print("Salário:",salario,"R$")
print("Estado Civil:",estado_civil)