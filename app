import csv
import re
from decimal import Decimal

with open("dados.csv",mode="r", encoding="utf-8") as arquivo,\
    open("saida_dados.csv",mode="w",encoding="utf-8",newline="") as arquivo_saida:
    writer = csv.writer(arquivo_saida,delimiter="|")

    writer.writerow(["Valor1", "Valor2, Diferenca"])

    for texto in arquivo:
        texto = texto.strip()

        if not texto:
            continue

        numeros = re.findall(r"\(([\d.,]+)\)", texto)
        numeros = [
            numero.replace(".","").replace(",",".")
            for numero in numeros
                
        ]
        
        if len(numeros) == 2:
            valor1 = Decimal(numeros[0])
            valor2 = Decimal(numeros[1])
            diferenca = abs(valor1 - valor2)
            writer.writerow([valor1,valor2,diferenca])
        else:
            print("Quantidade de valores diferente de 2")

print("Processo finalizado ")
        
