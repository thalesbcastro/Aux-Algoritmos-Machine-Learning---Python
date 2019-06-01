#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:34:16 2019

@author: thales
"""

'''
    Ler arquivo que contém os tempos do questionário
'''
import pandas as pd
#import numpy as np
import math
import random
import numpy as np

'''
    PARA RODAR O ALGORITMO COM O ARQUIVO ORIGINAL BASTA DESCOMENTAR A LINHA 21 E COMENTAR A 23
'''
#qt = pd.read_csv('./e_quiz_unique_IFRN.csv')
#Teste com um arquivo menor
qt = pd.read_csv('./e_quiz_menor_test.csv')

'''
    Transformando qt_timestart, qt_timefinish em um tipo datetime
'''
qt_timestart = pd.to_datetime(qt['qt_timestart'], unit='s')
qt_timefinish = pd.to_datetime(qt['qt_timefinish'], unit='s')
sub = []

'''
    Subtraindo qt_timefinish menos qt_timestart, transformando o resultado em timedelta (dias + horas).
    Convertendo a parcela de dias em minutos e a de horas também. Por fim, soma-se as duas parcelas
    e joga em uma lista para torná-la uma nova coluna no meu arquivo.
'''
#for i in range(qt_timefinish.size):

for i in range(qt_timestart.size):
    sub.append(
            math.floor(
                    (
                            
                            #Convertendo a parcela de dias para minutos
                            
                            (pd.to_timedelta(qt_timefinish[i] - qt_timestart[i], unit='d').days*24*60) 
                            + 
                            #Convertendo a parcela de horas para minutos     
                            ((pd.to_timedelta(qt_timefinish[i] - qt_timestart[i], unit='d').seconds)/60)
                            )
                    )
                )

'''
    Juntando o campo dos minutos ao arquivo.
'''
qt = qt.join(pd.DataFrame({'Tempo em minutos': sub}))

'''
    1 - poucos minutos <= 60 min
    2 - poucas horas 60 <= x <= 3*60 horas
    3 - Muitas horas > 3*60
'''

lista_tempos = []
lista_novos_tempos = []
q0 = []
q1 = []
q2 = []
q3 = []
q4 = []
q5 = []
q6 = []
q7 = []
q8 = []
q9 = []
u_name = []

i = 0
j = 0
while(j < qt_timestart.size):
    # verifico se os nomes são iguas nome e se o iterador não chegou no valor limite
    if qt['u_name'][j] == qt['u_name'][i] and (j + 1 != qt_timestart.size):
        # adiciono o tempo correspondente daquela linha
        lista_tempos.append(qt['Tempo em minutos'][j])
        # Apenas j varia, enquanto i permanece com seu valor inicial
        j = j + 1
    # verifico se chegou na última linha e se os nomes são iguais
    # Pois um problema que tava dando era que chegava na última linha e 
    # não se acrescentava os ultimos valores de tempo às colunas
    elif ((j + 1 == qt_timestart.size) and (qt['u_name'][j] == qt['u_name'][i])):
        #verifico se a lista é menor que 10 para completar com 0
        if len(lista_tempos) < 10:
            
            lista_tempos = (lista_tempos + [0]*10)[:10]
                
            #Criando as colunas separadas como uma lista
            q0.append(lista_tempos[0])
            q1.append(lista_tempos[1])
            q2.append(lista_tempos[2])
            q3.append(lista_tempos[3])
            q4.append(lista_tempos[4])
            q5.append(lista_tempos[5])
            q6.append(lista_tempos[6])
            q7.append(lista_tempos[7])
            q8.append(lista_tempos[8])
            q9.append(lista_tempos[9])
            u_name.append(qt['u_name'][i])
            j = j + 1 #Incremento j para poder sair do While
            #del lista_tempos[:] #Deleto a lista, mas nem precisava, pois esse é a última rodada
        else:
            # número de questionarios maior que 10. Pega-se os valores aleatoriamente
            lista_novos_tempos = random.sample(lista_tempos, 10)
            
            #Criando as colunas separadas como uma lista
            q0.append(lista_novos_tempos[0])
            q1.append(lista_novos_tempos[1])
            q2.append(lista_novos_tempos[2])
            q3.append(lista_novos_tempos[3])
            q4.append(lista_novos_tempos[4])
            q5.append(lista_novos_tempos[5])
            q6.append(lista_novos_tempos[6])
            q7.append(lista_novos_tempos[7])
            q8.append(lista_novos_tempos[8])
            q9.append(lista_novos_tempos[9])
            u_name.append(qt['u_name'][i])
            j = j + 1
            
        del lista_novos_tempos[:]  #Deleta-se mas nem precisava         
        del lista_tempos[:] # Deleta-se mas nem precisava
    # Esse é o caso que ele passou de um nome pra outro (joão, joão, joão, maria)
    # ou seja maria != joão. Nesse caso, não entra no primeiro if
    else:
        # verifico se a lista é menor que 10 para completar com 0
        if len(lista_tempos) < 10:
            lista_tempos = (lista_tempos + [0]*10)[:10]
                
            #Criando as colunas separadas como uma lista
            q0.append(lista_tempos[0])
            q1.append(lista_tempos[1])
            q2.append(lista_tempos[2])
            q3.append(lista_tempos[3])
            q4.append(lista_tempos[4])
            q5.append(lista_tempos[5])
            q6.append(lista_tempos[6])
            q7.append(lista_tempos[7])
            q8.append(lista_tempos[8])
            q9.append(lista_tempos[9])
            u_name.append(qt['u_name'][i])
            j = j + 1
            # Deve-se deletar os elementos da lista, pois ela será usada de novo de 0 a 9
            #del lista_tempos[:] 
        else:
            # número de questionarios maior que 10. Pega-se os valores aleatoriamente
            lista_novos_tempos = random.sample(lista_tempos, 10)
            
            #Criando as colunas separadas como uma lista
            q0.append(lista_novos_tempos[0])
            q1.append(lista_novos_tempos[1])
            q2.append(lista_novos_tempos[2])
            q3.append(lista_novos_tempos[3])
            q4.append(lista_novos_tempos[4])
            q5.append(lista_novos_tempos[5])
            q6.append(lista_novos_tempos[6])
            q7.append(lista_novos_tempos[7])
            q8.append(lista_novos_tempos[8])
            q9.append(lista_novos_tempos[9])
            u_name.append(qt['u_name'][i])
            # Deve-se deletar os elementos da lista, pois ela será usada de novo de 0 a 9
        del lista_novos_tempos[:]
        # Deve-se deletar os elementos da lista, pois ela será usada de novo de 0 a 9
        del lista_tempos[:] 
            # Como o i não varia, deve-se colocar o valor de j para a próxima rodada
        i = j
dict_questionarios = {'Alunos': u_name,'Q0': q0, 'Q1': q1, 'Q2': q2,
                      'Q3': q3, 'Q4': q4, 'Q5': q5, 'Q6': q6, 'Q7': q7,
                      'Q8': q8, 'Q9': q9}
quiz = pd.DataFrame(dict_questionarios, 
                                  columns=['Alunos', 'Q0', 'Q1', 'Q2', 'Q3',

                                           'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9'])


'''
    Com o valor do novo campo (o maior valor), n, criar id_q1, id_q2, id_q3,.., id_qn colunas e preenchê-las
    com a classificação acima (1 ou 2 ou 3) - comentário feito na reunião. 
    Nesse caso eu peguei a média pra cada aluno pra poder classificá-lo e
    na comparação, eu peguei o módulo dessa média
'''    
classe = []
for x in range(quiz.shape[0]):
    soma = quiz['Q0'][x] + quiz['Q1'][x]+ quiz['Q2'][x] + quiz['Q3'][x] + quiz['Q4'][x]+ quiz['Q5'][x] +quiz['Q6'][x] + quiz['Q7'][x]+ quiz['Q8'][x] + quiz['Q9'][x]
    # Somatório dos módulos
    #soma = math.fabs(quiz['Q0'][x]) + math.fabs(quiz['Q1'][x]+ quiz['Q2'][x]) + math.fabs(quiz['Q3'][x]) + math.fabs(quiz['Q4'][x]) + math.fabs(quiz['Q5'][x]) + math.fabs(quiz['Q6'][x]) + math.fabs(quiz['Q7'][x])+ math.fabs(quiz['Q8'][x]) + math.fabs(quiz['Q9'][x])
    modulo_soma = math.fabs(soma/10)
    n = 60 
    if modulo_soma <= n:
      classe.append(1)
      
    elif ((modulo_soma > n) and (modulo_soma <= 3*n)):
        classe.append(2)
        
    else:
        classe.append(3)

classe = pd.DataFrame({'Classificação': classe})
quiz = quiz.join(classe)

#Removo os duplicados
condicoes_Q0 = [
        (quiz['Q0'] <= 0),
        ((quiz['Q0'] > 0) & (quiz['Q0'] <= 60)),
        ((quiz['Q0'] > 60) & (quiz['Q0'] <= 3*60)),
        (quiz['Q0'] > 3*60)
        ]
condicoes_Q1 = [
        (quiz['Q1'] <= 0),
        ((quiz['Q1'] > 0) & (quiz['Q1'] <= 60)),
        ((quiz['Q1'] > 60) & (quiz['Q1'] <= 3*60)),
        (quiz['Q1'] > 3*60)
        ]
condicoes_Q2 = [
        (quiz['Q2'] <= 0),
        ((quiz['Q2'] > 0) & (quiz['Q2'] <= 60)),
        ((quiz['Q2'] > 60) & (quiz['Q2'] <= 3*60)),
        (quiz['Q2'] > 3*60)
        ]
condicoes_Q3 = [
        (quiz['Q3'] <= 0),
        ((quiz['Q3'] > 0) & (quiz['Q3'] <= 60)),
        ((quiz['Q3'] > 60) & (quiz['Q3'] <= 3*60)),
        (quiz['Q3'] > 3*60)
        ]
condicoes_Q4 = [
        (quiz['Q4'] <= 0),
        ((quiz['Q4'] > 0) & (quiz['Q4'] <= 60)),
        ((quiz['Q4'] > 60) & (quiz['Q4'] <= 3*60)),
        (quiz['Q4'] > 3*60)
        ]
condicoes_Q5 = [
        (quiz['Q5'] <= 0),
        ((quiz['Q5'] > 0) & (quiz['Q5'] <= 60)),
        ((quiz['Q5'] > 60) & (quiz['Q5'] <= 3*60)),
        (quiz['Q5'] > 3*60)
        ]
condicoes_Q6 = [  
        (quiz['Q6'] <= 0),
        ((quiz['Q6'] > 0) & (quiz['Q6'] <= 60)),
        ((quiz['Q6'] > 60) & (quiz['Q6'] <= 3*60)),
        (quiz['Q6'] > 3*60)
        ]
condicoes_Q7 = [       
        (quiz['Q7'] <= 0),
        ((quiz['Q7'] > 0) & (quiz['Q7'] <= 60)),
        ((quiz['Q7'] > 60) & (quiz['Q7'] <= 3*60)),
        (quiz['Q7'] > 3*60)
        ]
condicoes_Q8 = [  
        (quiz['Q8'] <= 0),
        ((quiz['Q8'] > 0) & (quiz['Q8'] <= 60)),
        ((quiz['Q8'] > 60) & (quiz['Q8'] <= 3*60)),
        (quiz['Q8'] > 3*60)
        ]
condicoes_Q9 = [
        (quiz['Q9'] <= 0),
        ((quiz['Q9'] > 0) & (quiz['Q9'] <= 60)),
        ((quiz['Q9'] > 60) & (quiz['Q9'] <= 3*60)),
        (quiz['Q9'] > 3*60)
        ]
resultados = [0, 1, 2, 3]

Q0_classe = np.select(condicoes_Q0, resultados)
Q1_classe = np.select(condicoes_Q1, resultados)
Q2_classe = np.select(condicoes_Q2, resultados)
Q3_classe = np.select(condicoes_Q3, resultados)
Q4_classe = np.select(condicoes_Q4, resultados)
Q5_classe = np.select(condicoes_Q5, resultados)
Q6_classe = np.select(condicoes_Q6, resultados)
Q7_classe = np.select(condicoes_Q7, resultados)
Q8_classe = np.select(condicoes_Q8, resultados)
Q9_classe = np.select(condicoes_Q9, resultados)

dict_classes = {'Q0': Q0_classe, 'Q1': Q1_classe, 'Q2': Q2_classe,
                      'Q3': Q3_classe, 'Q4': Q4_classe, 'Q5': Q5_classe, 'Q6': Q6_classe, 'Q7': Q7_classe,
                      'Q8': Q8_classe, 'Q9': Q9_classe}
classes_quiz = pd.DataFrame(dict_classes, 
                                  columns=['Q0', 'Q1', 'Q2', 'Q3',

                                           'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9'])


classe_individual = (classes_quiz.astype(int).sum(axis=1))/((classes_quiz != 0).astype(int).sum(axis=1))

#for x in range(quiz.shape[0]):
#    soma = Q0_classe[x] + Q1_classe[x] + Q2_classe[x] + Q3_classe[x] + Q4_classe[x] + Q5_classe[x] + Q6_classe[x] + Q7_classe[x] + Q8_classe[x] + Q9_classe[x]
#    soma = soma/10
##    n = round(soma)
#    classe_individual.append(round(soma))

classe_individual = pd.DataFrame({'Classificação_2': classe_individual})
quiz = quiz.join(classe_individual)
quiz.drop_duplicates(subset='Alunos', keep=False, inplace=True)

'''
    PARA GERAR O ARQUIVO CSV BASTA DESCOMENTAR A LINHA 211
'''

#quiz.to_csv('classificacao_questionarios.csv')
#quiz.to_excel('classificacao_questionario.xlsx')