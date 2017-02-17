#!/usr/bin/env python3
from cRBF import rbf_network as rbf_cython # radial basis function dalam cython yang telah dicompile
import numpy as np
from math import exp
import time

# fungsi evaluasi radial basis function dalam pure python
def rbf_pure(X, beta, theta):
    N = X.shape[0]
    D = X.shape[1]
    Y = np.zeros(N)
    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * exp(-(r * theta)**2)

    return Y

# init variabel
D = 5
N = 1000
X = np.array([np.random.rand(N) for d in range(D)]).T
beta = np.random.rand(N)
theta = 10

# hitung lamanya waktu eksekusi untuk pure python
start1 = time.time()
# jalankan fungsi di pure python
print('Processing pure python function....')
rbf_pure(X, beta, theta)
# selang waktu......
waktu1 = time.time()
T1 = waktu1-start1
print('Waktu Pure Python: %.4f seconds\n' %(T1))

# hitung lamanya waktu eksekusi untuk cython
start2 = time.time()
# jalankan fungsi di cython
print('Processing cython function....')
rbf_cython(X, beta, theta)
# selang waktu....
waktu2 = time.time()
T2 = waktu2-start2
print('Waktu Cython: %.4f seconds\n' %(T2))

print('Speedup = %.4f x' %(T1/T2))