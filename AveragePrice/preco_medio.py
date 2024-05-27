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

i=1
while i <= repeticao:
    try:
        lista_valores.append(float(input(f"Coloque o preço {i}: ")))
        lista_quantidade.append(int(input(f"Coloque a quantidade {i}: ")))
        i += 1
    except ValueError:
        print("Entrada inválida. Por favor, insira um valor numérico")

if repeticao > 0:
    mult_matriz = [x * y for x, y in zip(lista_valores, lista_quantidade)]
    soma_quantidade = sum(lista_quantidade)
    preco_medio = sum(mult_matriz) / soma_quantidade
    print(f"\nO Preço médio é: R$ {preco_medio: .2f} e a quantidade de ações são:{soma_quantidade: .0f}")
    if str(input("Gostaria de exportar o resultado em .txt? (y/n): ")).lower() == 'y':
        def obter_data_hora_atual():
            return datetime.now().strftime("%d/%m/%Y, %Hh%Mm%Ss")
        data_hora = obter_data_hora_atual()
        arquivo_txt = open('Py_Lessions\AveragePrice\dados_preco_medio.txt', 'w')
        caminho_absoluto = os.path.abspath('Py_Lessions\AveragePrice\dados_preco_medio.txt')
        arquivo_txt.write(f"Este arquivo está salvo em {caminho_absoluto}\nData e hora de criação:{data_hora}\n -------------------------")
        arquivo_txt.write("\n"*3)
        arquivo_txt.write(f"Preço médio: R$ {preco_medio}\nQuantidade: {soma_quantidade}")
        arquivo_txt.write(f"\n\nMemória de Cálculo:\nRepetição: {repeticao}\nLista de Preços: {lista_valores}\n")
        arquivo_txt.write(f"Lista de Quantidades: {lista_quantidade}\nMatriz de Preços: {mult_matriz}")
        arquivo_txt.write(f"\nObrigado por usar, desenvolvido por Caique.\n-------------------------")
        print(f"\nDados importados com sucesso em {caminho_absoluto}")
        print("\nObrigado por usar a calculadora de preço médio!")
        arquivo_txt.close()
    elif str(input("Gostaria de ver a memória de cálculo? (y/n): ")).lower == 'y':
        print("\nMemória de cálculo:")
        print(f"Repetição: {repeticao}\nLista de Preços: {lista_valores}")
        print(f"Lista de Quantidades: {lista_quantidade}\nMatriz de Preços: {mult_matriz}")
        print("\nObrigado por usar a calculadora de preço médio!")
    else:
        print("\nObrigado por usar a calculadora de preço médio!")
else:
    print("Nenhum dado inserido.")