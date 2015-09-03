from numba import njit

@njit
def numba_matmul(matA, matB, matC):
    for i in range(matC.shape[0]):
        for j in range(matC.shape[1]):
            tmp = 0
            for k in range(matA.shape[1]):
                tmp += matA[i, k] * matB[k, j]
            matC[i, j] = tmp


python_matmul = numba_matmul.py_func

import numpy as np
from ctypes import CDLL, c_double, c_int, POINTER, c_void_p


N = 128
A = B = np.random.random((N, N))
Cjit = np.zeros_like(A)
Cpy = np.zeros_like(A)
Ccc = np.zeros_like(A)
Cexp = np.dot(A, B)


dll = CDLL('./matmul.so')
c_matmul = dll.c_matmul
c_matmul.argtypes = [c_void_p,
                     c_void_p,
                     c_void_p,
                     c_int,
                     c_int,
                     c_int]

def run_numba():
    numba_matmul(A, B, Cjit)

def run_numpy():
    np.dot(A, B)

def run_python():
    python_matmul(A, B, Cpy)

def run_c():
    c_matmul(A.ctypes.data, B.ctypes.data, Ccc.ctypes.data,
             Ccc.shape[0], Ccc.shape[1], A.shape[1])

def test():
    run_numba()
    run_numpy()
    run_c()

    np.testing.assert_allclose(Cexp, Ccc)
    np.testing.assert_allclose(Cexp, Cjit)


"""
N = 1024
In [2]: %timeit run_numba()
1 loops, best of 3: 7.63 s per loop

In [3]: %timeit run_numpy()
10 loops, best of 3: 27.9 ms per loop

In [4]: %timeit run_c()
1 loops, best of 3: 7.56 s per loop


++++

N = 512

In [2]: %timeit run_c()
1 loops, best of 3: 197 ms per loop

In [3]: %timeit run_numba()
1 loops, best of 3: 194 ms per loop


"""


"""
+++++++++++++++++++++++++++++++++++++++++++

N = 64

In [2]: %timeit run_numba()
The slowest run took 673.90 times longer than the fastest. This could mean that an intermediate result is being cached
1000 loops, best of 3: 233 µs per loop

In [3]: %timeit run_python()
10 loops, best of 3: 108 ms per loop

In [4]: %timeit run_c()
1000 loops, best of 3: 238 µs per loop




N = 128

In [4]: %timeit run_python()
1 loops, best of 3: 877 ms per loop

In [2]: %timeit run_c()
100 loops, best of 3: 2.15 ms per loop

In [3]: %timeit run_numba()
The slowest run took 86.11 times longer than the fastest. This could mean that an intermediate result is being cached
1000 loops, best of 3: 1.93 ms per loop


N = 256

In [2]: %timeit run_python()
1 loops, best of 3: 6.85 s per loop

In [3]: %timeit run_c()
10 loops, best of 3: 24.4 ms per loop

In [4]: %timeit run_numba()
The slowest run took 6.93 times longer than the fastest. This could mean that an intermediate result is being cached
10 loops, best of 3: 26 ms per loop



N = 512

In [2]: %timeit run_python()
1 loops, best of 3: 54.7 s per loop

In [3]: %timeit run_numba()
1 loops, best of 3: 198 ms per loop

In [4]: %timeit run_c()
1 loops, best of 3: 204 ms per loop
"""

def plot():
    nn = np.array([64, 128, 256, 512])
    time_py = np.array([108 * 1000, 877 * 1000, 6.85*1000*1000, 54.7*1000*1000])
    time_c = np.array([238, 2150, 26*1000, 204*1000])
    time_jit = np.array([233, 1930, 24.4*1000, 198*1000])

    print('jit speedup', time_py / time_jit )
    print('c   speedup', time_py / time_c  )


if __name__ == '__main__':
    plot()
