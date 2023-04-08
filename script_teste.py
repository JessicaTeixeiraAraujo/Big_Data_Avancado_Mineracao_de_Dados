# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 19:21:11 2023

@author: Jessi
"""

import matplotlib.pyplot as plt
from seaborn import load_dataset
dados = load_dataset('tips')
dados['total_bill'].plot()
plt.show()
plt.clf()
dados['total_bill'].plot.hist()
plt.show()
plt.clf()
dados.plot.scatter(x='total_bill', y='tip')