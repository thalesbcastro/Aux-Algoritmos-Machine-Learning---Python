#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 14:48:45 2019

@author: thales
"""

import pandas as pd 


xls1 = pd.ExcelFile('Geral todos os alunos do IFRN com os EA Gustavo.xlsx')
xls2 = pd.ExcelFile('PRD-Dados sócio-acadêmicos-respostas 10-01-2012 - IFRN - GUSTAVO - Atual.xlsx')
#xls3 = pd.ExcelFile('Base de dados_mysql_IFRN_Rede Neural - 02-01-19 Gustavo.xlsx')
xls4 = pd.ExcelFile('fato_quantidades.xlsx')

df1 = xls1.parse(1) #Planilha referente ao xls1
df2 = xls2.parse(0) #Planilha referente ao xls2
#df3 = xls3.parse(1) #Planilha referente ao xls3
df4 = xls4.parse(0)
#nome_completo = sheet1['Nome_completo'].unique()

df1 = df1[df1.Registro_Bom != 0]
df2 = df2[df2.Registro_Bom != 0]
#df3 = df3[df3.Registro_Bom != 0]

dfmerge1 = pd.merge(df1, df2, on=['Nome_completo'], how='inner')

#dfmerge2 = pd.merge(dfmerge1, df3, on=['Nome_completo'], how='inner')
dfmerge2 = pd.merge(dfmerge1, df4, on=['Nome_completo'], how='inner')

ativo = []
for pontuacao in dfmerge2['PONTUAÇÃO ATIVO']:
    if pontuacao < 15:
        ativo.append(1)
    elif (pontuacao >= 15) and (pontuacao < 18):
        ativo.append(2)
    elif (pontuacao >= 18) and (pontuacao < 23):
        ativo.append(3)
    elif (pontuacao >= 23) and (pontuacao < 26):
        ativo.append(4)
    else:
        ativo.append(5)
        
df_ativo = pd.DataFrame({'Número Ativo': ativo})

reflexivo = []   
for pontuacao in dfmerge2['PONTUAÇÃO REFLEXIIVO']:
    if pontuacao < 16:
        reflexivo.append(1)
    elif (pontuacao >= 16) and (pontuacao < 20):
        reflexivo.append(2)
    elif (pontuacao >= 20) and (pontuacao < 24):
        reflexivo.append(3)
    elif (pontuacao >= 24) and (pontuacao < 27):
        reflexivo.append(4)
    else:
        reflexivo.append(5)

df_reflexivo = pd.DataFrame({'Número Reflexivo': reflexivo})

teorico = []        
for pontuacao in dfmerge2['PONTUAÇÃO TEORICO']:
    if pontuacao < 19:
        teorico.append(1)
    elif (pontuacao >= 19) and (pontuacao < 22):
        teorico.append(2)
    elif (pontuacao >= 22) and (pontuacao < 27):
        teorico.append(3)
    elif (pontuacao >= 27) and (pontuacao < 31):
        teorico.append(4)
    else:
        teorico.append(5)
        
df_teorico = pd.DataFrame({'Número Teórico': teorico})

pragmatico = []
for pontuacao in dfmerge2['PONTUAÇÃO PRAGMATICO']:
    if pontuacao < 21:
        pragmatico.append(1)
    elif (pontuacao >= 21) and (pontuacao < 23):
        pragmatico.append(2)
    elif (pontuacao >= 23) and (pontuacao < 29):
        pragmatico.append(3)
    elif (pontuacao >= 29) and (pontuacao < 32):
        pragmatico.append(4)
    else:
        pragmatico.append(5)

df_pragmatico = pd.DataFrame({'Número Pragmático': pragmatico})

df_grau1 = df_ativo.join(df_teorico)
df_grau2 = df_reflexivo.join(df_pragmatico)
df_final = df_grau1.join(df_grau2)

df_matrix = df_final.as_matrix()

numeros5 = 0
numeros4 = 0
column_5 = []
column_4 = []
vetor_ea = []
lista_perc = []
matrix_perc = dfmerge2.iloc[:, 48:52]
matrix_perc = matrix_perc.as_matrix()

for i in range(df_matrix.shape[0]):
    '''
        for pra contar a quantidades de 5's e 4's, bem como guardar a respectiva posição
        da coluna. Por exemplo, a linha é [5, 4, 4 e 5], tem dois 5's (numeros5=2) e está na
        coluna 0 e 3 (column_5 = [0, 3]). Mesma coisa serve pro 4.
    '''
    for j in range(df_matrix.shape[1]):
        if df_matrix[i, j] == 5:
            numeros5 += 1
            column_5.append(j)
        elif df_matrix[i, j] == 4:
            numeros4 += 1
            column_4.append(j)
    
    '''
        Para os casos em que a linha tem apenas um 5 ou um 4, significa que numeros5 = 1 ou 
        numeros4 = 1 e como só entrou uma vez no if ou no elif, a lista column_4 ou lista column_5
        tem apenas um elemento, indice = 0. Logo a comparação é feita com a posição 0 da lista (um elemento).
        Se a posição da coluna for 0, ele vai ser Ativo, se for 1, vai ser Teórico, etc. 
    '''       
    if numeros5 == 1:
        if column_5[0] == 0:
            vetor_ea.append('Ativo')
       
        elif column_5[0] == 1:
            vetor_ea.append('Teorico')
        
        elif column_5[0] == 2:
            vetor_ea.append('Reflexivo')
        
        else:
            vetor_ea.append('Pragmatico')
        
    
    #Pra o caso de mais de 2 4's, a linha não pode conter nenhum 5.
    elif numeros4 == 1 and numeros5 == 0:
        if column_4[0] == 0:
            vetor_ea.append('Ativo')
            
        elif column_4[0] == 1:
            vetor_ea.append('Teorico')
            
        elif column_4[0] == 2:
            vetor_ea.append('Reflexivo')
            
        else:
            vetor_ea.append('Pragmatico')

#        Pro caso em que há mais de 2 5's ou 2 4's, cria-se uma lista com os números correspondentes em porcentagem
#        por meio de um for de 0 ao len(column_5) e verifica-se qual valor é o maior entre eles. Depois cria-se um
#        for com 4 posições que verifica qual é a coluna que corresponde aquele máximo na matriz de porcentagem.
#        Depois que estiver com a posição da coluna, acrescenta-se os EA's.   
        
    elif numeros5 >= 2:
        for k in range(len(column_5)):
            lista_perc.append(matrix_perc[i, column_5[k]])
        #Retornar o index do maior elemento da matriz de porcentagem
        maximo = max(lista_perc)
        indice = 0
        for m in range(4):
            if matrix_perc[i, m] == maximo:
                indice = m
        if indice == 0:
            vetor_ea.append('Ativo')
            
        elif indice == 1:
            vetor_ea.append('Teorico')
            
        elif indice == 2:
            vetor_ea.append('Reflexivo')
            
        else:
            vetor_ea.append('Pragmatico')
            
        del lista_perc[:]

#        Pro caso em que há mais de 2 5's ou 2 4's, cria-se uma lista com os números correspondentes em porcentagem
#        por meio de um for de 0 ao len(column_5) e verifica-se qual valor é o maior entre eles. Depois cria-se um
#        for com 4 posições que verifica qual é a coluna que corresponde aquele máximo na matriz de porcentagem.
#        Depois que estiver com a posição da coluna, acrescenta-se os EA's.
        
        
    elif numeros4 >= 2 and numeros5 == 0:
        for k in range(len(column_4)):
            lista_perc.append(matrix_perc[i, column_4[k]])
        #Retornar o index do maior elemento da matriz de porcentagem
        indice = 0
        maximo = max(lista_perc)
        for m in range(4):
            if matrix_perc[i, m] == maximo:
                indice = m
        if indice == 0:
            vetor_ea.append('Ativo')
            
        elif indice == 1:
            vetor_ea.append('Teorico')
            
        elif indice == 2:
            vetor_ea.append('Reflexivo')
            
        else:
            vetor_ea.append('Pragmatico')
            
        del lista_perc[:]
             
    else:
         vetor_ea.append('Indefinido')
         
    del column_4[:]
    del column_5[:]
    numeros4 = 0
    numeros5 = 0

df_ea = pd.DataFrame({'estilo_de_aprendizagem': vetor_ea})
dfmerge2 = dfmerge2.join(df_ea)
df_ea = pd.DataFrame(dfmerge2, columns =['Nome_completo', 'qtd_de_acessos_pagina', 'qtd_de_acessos_pasta', 'qtd_de_acessos_arquivo', 'qtd_de_acessos_url',
                                         'numero_de_acesso_por_curso', 'qtd_mensagens_enviadas', 'qtd_de_acessos_livro', 'qtd_acessos_ao_chat', 
                                         'qtd_mensagens_chat', 'qtd_acessos_wiki', 'numero_postagens',  
                                         'qtd_de_acessos_tarefa', 'qtd_de_acessos_forum', 'qtd_de_acessos_questionario', 'estilo_de_aprendizagem'] ) 

df_ea.to_csv('comportamentos_alunos_ifrn_definitivo.csv')
'''
    Juntando os campos Número Ativo, Número Teórico, Número Reflexivo e Número Pragmático ao 
    df_merge2, onde tem todas as informações. 
'''
