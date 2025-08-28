#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 08:57:01 2017

@author: inbu
"""

from sklearn import datasets
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

#import Iris data set

iris = datasets.load_iris()
X = iris.data
y = iris.target

plt.figure()
plt.scatter(X[:,0], X[:,1], c=y)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()

def doPCA():
    pca = PCA(n_components=3) 
    pca.fit(X)
    return pca

pca = doPCA()
print(pca.explained_variance_ratio_)

X_reduced = pca.fit_transform(X)
plt.figure()
plt.scatter(X_reduced[:,0], X_reduced[:,1],c=y)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()



import hoggorm as ho
import hoggormplot as hopl
    
model01 = ho.nipalsPCA(arrX=X, Xstand=True, cvType=["loo"], numComp=4)

 
hopl.plot(model01, plots=[1, 2, 3, 6], cumulative=True, line=True)


hopl.plot(model01)

hopl.plot(model01, plots=['scores', 'loadings', 'explainedVariance'], cumulative=True)   

