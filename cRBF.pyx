from libc.math cimport exp   # fungsi eksponen dalam library C
from math import exp as exp2 # fungsi eksponen dalam python
import numpy as np

cdef class Cython_vs_Python(object):
    # Pake pure Python (deklarasi variabel dan library semua dari python)
    def Python(self, X, beta, theta): 
        N = X.shape[0]
        D = X.shape[1]
        Y = np.zeros(N)
        r = 0

        for i in range(N):
            for j in range(N):
                r = 0
                for d in range(D):
                    r += (X[j, d] - X[i, d]) ** 2
                r = r**0.5
                Y[i] += beta[j] * exp2(-(r * theta)**2)

        return Y

    # Pake Cython (deklarasi variabel dengan gaya sintaks bahasa C dan library dari C)
    cdef double[:] Cython(self, double[:, :] X,  double[:] beta, double theta):
        cdef int N = X.shape[0]
        cdef int D = X.shape[1]
        cdef double[:] Y = np.zeros(N)
        cdef int i, j, d
        cdef double r = 0

        for i in range(N):
            for j in range(N):
                r = 0
                for d in range(D):
                    r += (X[j, d] - X[i, d]) ** 2
                r = r**0.5
                Y[i] += beta[j] * exp(-(r * theta)**2)

        return Y


    def rbf_python(self, X, beta, theta):
        self.Python(X, beta, theta)

    def rbf_cython(self, double[:, :] X,  double[:] beta, double theta):
        self.Cython(X, beta, theta)