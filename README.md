# Cython vs Python

Dalam repositori ini akan membandingkan kecepatan eksekusi dari program yang menggunakan Cython dan pure Python.

Sekarang ini, python merupakan bahasa pemrograman yang cukup populer. Banyak framework dan library yang berhubungan dengan perkembangan teknologi seperti data science dan deep learning menggunakan python, misalnya [TensorFlow](https://www.tensorflow.org/). Seperti yang diketahui bahwa bahasa interpreter seperti python untuk eksekusinya memakan waktu yang cukup lama. Apalagi jika untuk mengolah data yang cukup besar misalnya dalam deep learning, akan memakan lebih banyak sumber daya.

Cython adalah versi compilernya dari python yang menggunakan compiler bahasa C seperti GCC dan MinGW. Jadi, bahasa pemrograman interpreter python yang terbilang cukup mudah dan didukung banyak library seperti deep learning, dapat memiliki performa seperti bahasa C karena dicompile kedalam bahasa mesin.


## Setup
Versi python yang digunakan adalah versi 3.5 dan sistem operasi yang digunakan adalah Linux 64-bit.

- Instal pip (jika belum ada):
```sh
$ sudo apt-get install python3-pip python3-dev
```
- Langsung install package Cython
```sh
$ sudo python3 -m pip install cython
```

## Studi Kasus
Contoh studi kasus yang akan dikerjakan yaitu mengevaluasi skema pendekatan dari [Radial Basis Function (RBF)](http://en.wikipedia.org/wiki/Radial_basis_function). 

![function](https://github.com/agungdwiprasetyo/cython-vs-python/raw/master/pic/rbf.png)

Pertama buat dahulu program cython. File cython biasanya berekstensi ```*.pyx```. Program cython yang telah dibuat untuk mengevaluasi Radial Basis Function yaitu dapat dilihat pada file ```cRBF.pyx```. 

**cRBF.pyx**
```python
from libc.math cimport exp 
import numpy as np

def rbf_network(double[:, :] X,  double[:] beta, double theta):
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
```

Untuk mengcompilenya buat dahulu file ```setup.py``` 

**setup.py**
```python
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules=[ Extension("cRBF",
              ["cRBF.pyx"],
              libraries=["m"],
              extra_compile_args = ["-ffast-math"])]

setup(
  name = "cRBF",
  cmdclass = {"build_ext": build_ext},
  ext_modules = ext_modules)
```

Kemudian jalankan perintah pada terminal:
```sh
$ python3 setup.py build_ext --inplace
```
Jika sukses (tidak terdapat error) maka tampilan proses seperti gambar dibawah ini:

![progress](https://github.com/agungdwiprasetyo/cython-vs-python/raw/master/pic/processbuild.png)

Dapat dilihat hasil compile program dalam bahasa mesin terdapat dalam folder ```/build/temp.linux-x86_64-3.5```.

Setelah sukses mengcompile, kita dapat mengimpor fungsi dalam bahasa cython tadi ke dalam program python, yaitu dengan membuat potongan program seperti berikut:
```python
import cRBF
rbf = cRBF.Cython_vs_Python()
# cRBF -> nama file cython yang telah dicompile
# Cython_vs_Python -> nama class dalam program cython tersebut
```

Langkah selanjutnya yaitu membandingkan waktu eksekusi dari program yang menggunakan pure native python dengan program cython yang telah dicompile tadi. Dalam proses perbandingan ini menggunakan Jupyter Notebook (IPython). 

![console](https://github.com/agungdwiprasetyo/cython-vs-python/raw/master/pic/console.png)

Dapat dilihat pada line pertama menggunakan pure native python yang eksekusi programnya memakan waktu selama 11.3 sekon. Sedangkan pada program yang menggunakan cython pada line kedua waktu eksekusinya jauh lebih singkat yaitu 101 milisekon. Sungguh peningkatan performa yang cukup signifikan.

## Compare
Akan dibandingkan kecepatan eksekusi dari program yang dijalankan dalam local function python, pure python dalam class cython, dan cython. Program dapat dilihat dalam file ```cRBF.pyx```. Untuk memulai perbandingan, lakukan perintah di terminal seperti berikut:
```sh
# clone this repository
$ git clone https://github.com/agungdwiprasetyo/cython-vs-python

# change directory
$ cd cython-vs-python

# compile cRBF.pyx
$ python3 setup.py build_ext --inplace

# run program
$ ./testSpeedup.py
```

Maka hasilnya seperti berikut:

![compare](https://github.com/agungdwiprasetyo/cython-vs-python/raw/master/pic/compare.png)

Dapat dilihat dari hasil diatas, fungsi dalam class yang menggunakan cython memakan waktu eksekusi yang paling singkat, karena menggunakan gaya penulisan sintaks program dan library dari bahasa C (dapat dilihat dalam file [cRBF.pyx](https://github.com/agungdwiprasetyo/cython-vs-python/blob/master/cRBF.pyx) ).

Untuk melihat interaksi antara Python dan C dalam Cython, jalankan perintah seperti berikut:
```sh
$ cython cRBF.pyx -a
```
Akan terbentuk file **cRBF.html**. Buka file tersebut, maka seperti gambar dibawah ini:

![interaction](https://github.com/agungdwiprasetyo/cython-vs-python/raw/master/pic/interaction.png)

Baris program yang berwarna kuning menandakan interaksi antara sintaks Python dan C. Semakin sedikit interaksi ini maka waktu eksekusi program akan semakin cepat.

sumber -> [Cython: C-Extensions for Python](http://cython.org/)
