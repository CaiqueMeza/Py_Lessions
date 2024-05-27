import os
from datetime import datetime

try:
    repeticao = int(input("Quantas vezes você precisa inserir o preço e a quantidade? "))
except ValueError:
    print("Digite um número inteiro.")
    repeticao = 0

lista_valores = []
lista_quantidade = []
mult_matriz = []
PM_iteracao = []
quant_iterada = []

i = 1
while i <= repeticao:
    try:
        preco = float(input(f"Coloque o preço {i}: "))
        quantidade = int(input(f"Coloque a quantidade {i}: "))
        lista_valores.append(preco)
        lista_quantidade.append(quantidade)
        i += 1
    except ValueError:
        print("Entrada inválida. Por favor, insira um valor numérico")

if repeticao > 0:
    mult_matriz = [x * y for x, y in zip(lista_valores, lista_quantidade)]
    soma_quantidade = sum(lista_quantidade)
    preco_medio = sum(mult_matriz) / soma_quantidade
    
    # Calcular PM_iteracao e quant_iterada
    soma_parcial = 0
    for index in range(repeticao):
        soma_parcial += lista_quantidade[index]
        quant_iterada.append(soma_parcial)
        PM_iteracao.append(sum(mult_matriz[:index+1]) / quant_iterada[index])

    print(f"\nO Preço médio é: R$ {preco_medio:.2f} e a quantidade de ações são: {soma_quantidade:.0f}")
    
    if str(input("Gostaria de exportar o resultado em .txt? (y/n): ")).lower() == 'y':
        def obter_data_hora_atual():
            return datetime.now().strftime("%d/%m/%Y, %Hh%Mm%Ss")
        
        data_hora = obter_data_hora_atual()
        caminho_relativo = 'Py_Lessions/AveragePrice/dados_preco_medio.txt'
        caminho_absoluto = os.path.abspath(caminho_relativo)
        
        with open(caminho_relativo, 'w') as arquivo_txt:
            arquivo_txt.write(f"Este arquivo está salvo em {caminho_absoluto}\nData e hora de criação: {data_hora}\n-------------------------\n\n")
            arquivo_txt.write(f"Preço médio: R$ {preco_medio:.2f}\nQuantidade: {soma_quantidade}\n\n")
            arquivo_txt.write(f"Memória de Cálculo:\nRepetição: {repeticao}\nLista de Preços: {lista_valores}\nLista de Quantidades: {lista_quantidade}\n")
            arquivo_txt.write(f"Matriz de Preços: {mult_matriz}\nQuantidade Iterada: {quant_iterada}\nPM Iterado: {PM_iteracao}\n")
            arquivo_txt.write("\nObrigado por usar, desenvolvido por Caique.\n-------------------------")
        
        print(f"\nDados exportados com sucesso em {caminho_absoluto}")
    elif str(input("Gostaria de ver a memória de cálculo? (y/n): ")).lower() == 'y':
        print("\nMemória de cálculo:")
        print(f"Repetição: {repeticao}\nLista de Preços: {lista_valores}")
        print(f"Lista de Quantidades: {lista_quantidade}\nMatriz de Preços: {mult_matriz}")
        print(f"Quantidade Iterada: {quant_iterada}\nPM Iterado: {PM_iteracao}")
    else:
        print("\nObrigado por usar a calculadora de preço médio!")
else:
    print("Nenhum dado inserido.")