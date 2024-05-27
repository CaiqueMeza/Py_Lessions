from datetime import datetime as dt, timedelta as td #biblioteca para maniputação de datas

print("Bem vindo à Calculadora de Multas de Livros!")

i = 'sim' #condição verdadeira para o looping de execução

while i == 'sim':
    #recebe as informações do usuário
    input_inicio = input("Qual a data de retirada? (dd/mm/aaaa): ")
    input_devolucao = input("Qual a data de devolução? (dd/mm/aaaa): ")

    #strptime transforma uma string em formato data para maniputações futuras
    input_inicio_valor = dt.strptime(input_inicio, "%d/%m/%Y")
    input_devolucao_valor = dt.strptime(input_devolucao, "%d/%m/%Y")

    #timestamp transforma os valores datetime no padrão em segundos para manipulação
    numero_data_inicio = input_inicio_valor.timestamp()
    numero_data_devolucao = input_devolucao_valor.timestamp()

    #determina a data limite para devolução
    data_limite = input_inicio_valor + td(days=5)
    limitestamp = data_limite.timestamp()

    #retorna a diferença entre a data de retirada e devolução
    dif_em_dias = int((numero_data_devolucao - numero_data_inicio) / (60 * 60 * 24))

    #retorna a diferença entre a data limite e devolução
    dif_em_dias_atraso = int((numero_data_devolucao - limitestamp) / (60 * 60 * 24))

    #transforma a data limite em formato para string
    data_limite_valor2 = dt.strftime(data_limite, "%d/%m/%Y")
    
    #não considerar diferenças de datas negativas
    if dif_em_dias_atraso < 0:
        dif_em_dias_atraso = 0

    #aperfeiçoamento do código
    atraso1 = dif_em_dias_atraso <= 3
    atraso2 = dif_em_dias_atraso >= 4 and dif_em_dias_atraso <= 7
    atraso3 = dif_em_dias_atraso > 7

 
  

    #condições
    #entregou antes ou igual à data limite
    if data_limite >= input_devolucao_valor:
        print(f"A devolução limite era para a data {data_limite_valor2}. Sem multa")
        i = input("gostaria de testar novamente? (sim/não): ")

    #entregou depois da data limite
    elif data_limite < input_devolucao_valor:

        #entregou entre 1 a 3 dias de atraso
        if  atraso1 == True:
            multa = 0.5 * dif_em_dias_atraso
            dias_proxima_multa = 4 - dif_em_dias_atraso
            proxima_multa = 1.00

        #entregou entre 4 a 7 dias de atraso    
        elif atraso2 == True:
            multa = 1 * dif_em_dias_atraso
            dias_proxima_multa = 8 - dif_em_dias_atraso
            proxima_multa = 2.00

        #entregou acima de 7 dias de atraso    
        elif atraso3 == True:
            multa = 2 * dif_em_dias_atraso
            dias_proxima_multa = None  # Já está na multa máxima
            proxima_multa = None

        
        #saída para o usuário
        if proxima_multa is not None:
            print(f"Você devolveu com {dif_em_dias_atraso} dias de atraso. Neste caso a multa será de R$ {multa}")
            print(f"A multa foi de R$ {multa/dif_em_dias_atraso} por dia de atraso")
            print(f"Se demorasse mais {dias_proxima_multa} dias, a multa passaria a ser de R$ {proxima_multa} por dia")
        else:
            print(f"Você devolveu com {dif_em_dias_atraso} dias de atraso. Neste caso a multa será de R$ {multa}")
            print(f"A multa foi de R$ {multa/dif_em_dias_atraso} por dia de atraso")

        i = input("gostaria de testar novamente? (sim/não): ")
        print("Obrigado por usar a calculadora de multas!")