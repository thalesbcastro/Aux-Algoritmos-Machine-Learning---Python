#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:47:59 2019

@author: thales
"""
#import numpy as np 
import pandas as pd

#time_quiz = pd.read_csv('./e_quiz_unique_IFRN.csv')
#time_glossary = pd.read_csv('./e_glossary_IFRN.csv')
#time_choose = pd.read_csv('./e_tempo_escolha.csv')
time_assig = pd.read_csv('./e_tempo_tarefa.csv')

'''
    Modificando o arquivo e_quiz_unique.csv
'''
#time_quiz['q_timeopen'] = pd.to_datetime(time_quiz['q_timeopen'], unit='s')
#time_quiz['qt_timestart'] = pd.to_datetime(time_quiz['qt_timestart'], unit='s')
#time_quiz['qt_timefinish'] = pd.to_datetime(time_quiz['qt_timefinish'], unit='s')
#
#time_quiz['tempo_total_respondendo'] = time_quiz['qt_timefinish'] - time_quiz['qt_timestart'] 
#time_quiz['tempo_criacao_menos_primeiro_acesso'] = time_quiz['qt_timestart'] - time_quiz['q_timeopen'] 
#
#time_quiz.to_csv('tempos_questionarios.csv')


'''
    Modificando o arquivo e_glossary_IFRN.csv
'''

#time_glossary['tempo_criacao_item'] = pd.to_datetime(time_glossary['tempo_criacao_item'], unit='s')
#time_glossary['tempo_modificacao_item'] = pd.to_datetime(time_glossary['tempo_modificacao_item'], unit='s')
#time_glossary['tempo_criacao_glossario'] = pd.to_datetime(time_glossary['tempo_criacao_glossario'], unit='s')
#time_glossary['tempo_modificacao_glossario'] = pd.to_datetime(time_glossary['tempo_modificacao_glossario'], unit='s')
#
#
#time_glossary.to_csv('tempos_do_glossario.csv')

'''
    Modificando o arquivo e_tempo_escolha.csv
'''

#time_choose['tempo_inicial'] = pd.to_datetime(time_choose['tempo_inicial'], unit='s')
#time_choose['tempo_resposta'] = pd.to_datetime(time_choose['tempo_resposta'], unit='s')
#
##time_choose['tempo_que_levou_pra_responder'] = time_choose['tempo_resposta'] - time_choose['tempo_inicial']
#time_choose.to_csv('tempos_atividade_resposta.csv')


'''
    Modificando o arquivo e_tempo_tarefa.csv
'''

time_assig['data_entrega'] = pd.to_datetime(time_assig['data_entrega'], unit='s')
time_assig['prazo_entrega'] = pd.to_datetime(time_assig['prazo_entrega'], unit='s')
time_assig['tempo_que_levou_pra_entregar'] = time_assig['prazo_entrega'] - time_assig['data_entrega'] 

#time_choose['tempo_que_levou_pra_responder'] = time_choose['tempo_resposta'] - time_choose['tempo_inicial']
#time_assig.to_csv('tempos_atividade_tarefa.csv')