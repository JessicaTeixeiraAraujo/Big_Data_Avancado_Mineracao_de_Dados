# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 19:46:47 2023

@author: Jessi
"""
!pip install kneed
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from kneed import KneeLocator


X, _ = make_blobs(n_samples=200, random_state=42, centers=4)
lista_x = []
lista_y = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    lista_x.append(k)
    lista_y.append(kmeans.inertia_)
knee = KneeLocator(lista_x, lista_y, curve='convex',
                   direction='decreasing')
knee.plot_knee()
melhor_k = lista_x[knee.knee-2]
print('Melhor k:', melhor_k)