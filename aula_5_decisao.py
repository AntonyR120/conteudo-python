media = float(input("Digite o valor da média: "))
if media <= 10:
    if media >= 0:
        if media >= 7:
            print("Parebéns, você está aprovado! 😊")
        elif media >= 3:
            print("Atenção, você está de exame! 🤣")
        else:
            print("Que pena, você está reprovado! 😒")