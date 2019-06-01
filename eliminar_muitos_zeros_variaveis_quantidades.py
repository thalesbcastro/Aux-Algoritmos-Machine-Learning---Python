#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:55:12 2019

@author: thales
"""

'''
    Pegar só as variáveis de entrada e transformar em 0 ou 1. 1 pra aquilo que for diferente de
    zero e 0 pra aquilo que for 0. [Nova Matriz] = ([matriz] != 0) // [[0, 0, 1, 1, 0,.., 1], ...]
    
'''
import pandas as pd 
import matplotlib.pyplot as plt; plt.rcdefaults()

datatrain = pd.read_csv('./comportamentos_alunos_ifrn_definitivo.csv')
datatrain = datatrain.iloc[:, 1:16]

datatrain.loc[datatrain['estilo_de_aprendizagem']=='Indefinido','estilo_de_aprendizagem'] = 0
datatrain.loc[datatrain['estilo_de_aprendizagem']=='Ativo',     'estilo_de_aprendizagem'] = 1
datatrain.loc[datatrain['estilo_de_aprendizagem']=='Teorico',   'estilo_de_aprendizagem'] = 2
datatrain.loc[datatrain['estilo_de_aprendizagem']=='Reflexivo', 'estilo_de_aprendizagem'] = 3
datatrain.loc[datatrain['estilo_de_aprendizagem']=='Pragmatico','estilo_de_aprendizagem'] = 4

matriz_corr = datatrain.corr()

import numpy as np
 
objects = ('v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7',
           'v8', 'v9', 'v10', 'v11', 'v12', 'v13')
y_pos = np.arange(len(objects))
last_row = matriz_corr.iloc[14, :14]
performance = np.array(last_row)
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Valor da respectiva coluna')
plt.title('Gráfico de barras da última linha da matriz de correlação')
plt.show()
## Pegando apenas os valores das variáveis   
#matriz_qtd = datatrain.iloc[:, 1:15]
#
## Dividindo a matriz por ela mesma pra ficar 0 ou 1
#matriz_qtd = matriz_qtd/matriz_qtd
#
##matriz_table = matriz_qtd.apply(pd.to_numeric)
##matriz_table = matriz_table.as_matrix()
## Como 0/0 dá uma indetermiinação, ele coloca um NaN no lugar
## Logo troca-se o NaN por 0 na seguinte linha
#matriz_qtd.fillna(0, inplace=True)
##matriz_table = datatrain.as_matrix()
#'''
#    Criar uma nova coluna com o somatório de 1's daquela linha correspondente.
#'''
#matriz_qtd['Somatório das linhas'] = matriz_qtd.sum(axis=1)
##novo_dataframe = datatrain.iloc[:, 0:1]
##matriz_qtd = matriz_qtd.join(datatrain.iloc[:, 15:16])
#matriz_qtd = matriz_qtd[matriz_qtd['Somatório das linhas'] >= 7]
#matriz_qtd = matriz_qtd.drop(['Somatório das linhas'], axis=1)
##novo_dataframe = novo_dataframe.join(datatrain.iloc[:,15:16])
#
#'''
#    Para criar o arquivo csv é preciso descomentar a linha seguinte 
#'''
#matriz_qtd.to_csv('zero_um_menos_50_alunos.csv')
