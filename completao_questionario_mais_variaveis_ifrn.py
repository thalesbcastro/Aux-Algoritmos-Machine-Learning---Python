#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:12:50 2018

@author: thales
"""
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


todasTurmas = pd.read_excel("Questionario_IFRN.xlsx")
comportamentosAlunos = pd.read_excel("variaveis_mysql_IFRN_correções.xlsx")
#X = np.array(todasTurmas.iloc[:, 50:54].values)
#
#kmeans = KMeans(n_clusters = 4, random_state = 0)
#kmeans.fit(X)

df = todasTurmas.iloc[:, :]
#df['k-Grupos'] = kmeans.labels_

#sb.pairplot(df, hue='k-Grupos')

df['Aluno'] = todasTurmas.iloc[:, 0].values
df_1 = comportamentosAlunos.iloc[:, 0:15]

#junção dos dataframes pelo campo Alunos
df_merge = pd.merge(df, df_1, on=['Aluno'], how='outer')
 
# def_merge -> Junta os arquivos pelo campo "Aluno" e acrescenta os demais campos. 
# O aluno que tem seu nome em um e não tem no outro, os respectivos campos são preenchidos com NaN
#retirando do dataframe NaN
df_completo = df_merge.dropna()

#Transformando em xlsx 
writer = pd.ExcelWriter('questionarioCHAEA_mais_variaveisSQL.xlsx')
df_completo.to_excel(writer, 'sheet1')
writer.save()