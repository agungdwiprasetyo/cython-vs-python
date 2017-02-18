#!/usr/bin/env python3
import cRBF # radial basis function dalam cython yang telah dicompile
import numpy as np
from math import exp
import time

# fungsi evaluasi radial basis function dalam local function pure python
def rbf_pure_local(X, beta, theta):
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

# init class dalam cython yg telah dicompile
rbf = cRBF.Cython_vs_Python()

# 1. hitung lamanya waktu eksekusi untuk local function pure python
start = time.time()
# jalankan fungsi di pure python
print('Processing pure python in local function....')
rbf_pure_local(X, beta, theta)
# selang waktu......
finish = time.time()
T1 = finish-start

# 2. hitung lamanya waktu eksekusi untuk pure python dalam class cython (cRBF)
start = time.time()
# jalankan fungsi di cython
print('Processing pure python in class....')
rbf.rbf_python(X, beta, theta)
# selang waktu....
finish = time.time()
T2 = finish-start

# 3. hitung lamanya waktu eksekusi untuk cython dalam class cython cRBF
start = time.time()
# jalankan fungsi di cython
print('Processing cython class....')
rbf.rbf_cython(X, beta, theta)
# selang waktu....
finish = time.time()
T3 = finish-start

print('\nHasil:')
print('Waktu eksekusi Pure Python dalam local function : %.4f seconds\n' %(T1))
print('Waktu eksekusi Pure Python dalam class          : %.4f seconds\n' %(T2))
print('Waktu eksekusi Cython dalam class               : %.4f seconds\n' %(T3))