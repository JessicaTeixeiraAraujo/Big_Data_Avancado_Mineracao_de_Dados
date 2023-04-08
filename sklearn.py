# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 19:52:43 2023

@author: Jessi
"""

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import f1_score

def varia_k(X, Y):
    for k in range(1, 16, 2):
        knn = KNeighborsClassifier(n_neighbors=k)
        previsoes = cross_val_predict(knn, X, Y, cv=10)
        f1score = f1_score(Y, previsoes, average='weighted')
        print('K =', k, ':', round(f1score, 4))

dados = datasets.load_digits()
X, Y = dados.data, dados.target
print('Base de dados digits, f1-score variando k:')
varia_k(X, Y)