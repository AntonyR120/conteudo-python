tamanho_arquivo = float(input("Digite o tamanho do arquivo em MBs: "))
velocidade_link = float(input("Digite a velocidade da internet: "))
tmp_se = tamanho_arquivo / velocidade_link
tmp_min = tmp_se / 60
print("O tempo aproximado de dowload será de: ",tmp_min,"minutos")