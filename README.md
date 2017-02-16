# Cython vs Python

Dalam repositori ini akan membandingkan kecepatan eksekusi dari program yang menggunakan Cython dan pure Python.

Seperti yang diketahui bahwa bahasa interpreter seperti python untuk eksekusinya memakan waktu yang cukup lama. Cython adalah versi compilernya dari python yang menggunakan compiler bahasa C seperti GCC dan MinGW. Jadi, bahasa pemrograman interpreter python yang terbilang cukup mudah dapat memiliki performa seperti bahasa C karena dicompile kedalam bahasa mesin.

## Setup
Versi python yang digunakan adalah versi 3.5 dan sistem operasi yang digunakan adalah Linux 64-bit.

- Instal pip (jika belum ada):
```sh
$ sudo apt-get install python-pip python-dev
```
- Download whl binary file:
```sh
$ export CT_BINARY_URL=https://pypi.python.org/packages/11/a4/4e93591fcf898a229579b0fd02fe2fd9326b9bb3ce34ceee4a2b87937ca1/Cython-0.25.2-cp35-cp35m-manylinux1_x86_64.whl
```
- Install binary file yang telah didownload:
```sh
$ sudo pip3 install --upgrade $CT_BINARY_URL
```

## Studi Kasus
Contoh studi kasus yang akan dikerjakan yaitu mengevaluasi skema pendekatan dari [Radial Basis Function (RBF)](http://en.wikipedia.org/wiki/Radial_basis_function). 

Pertama buat dahulu program cython, kemudian dicompile. File cython biasanya berekstensi ```*.pyx```. Program cython yang telah dibuat untuk mengevaluasi Radial Basis Function yaitu dapat dilihat pada file ```cRBF.pyx```. Untuk mengcompilenya buat dahulu file ```setup.py``` kemudian jalankan perintah pada terminal:
```sh
$ python3 setup.py build_ext --inplace
```
Jika sukses (tidak terdapat error) maka tampilan proses seperti gambar dibawah ini:

![progress](https://github.com/agungdwiprasetyo/cython-vs-python/raw/master/pic/processbuild.png)

Dapat dilihat hasil compile program dalam bahasa mesin terdapat dalam folder ```/build/temp.linux-x86_64-3.5```.

Setelah sukses mengcompile, kita dapat mengimpor fungsi dalam bahasa cython tadi ke dalam program python, yaitu dengan membuat potongan program seperti berikut:
```python
from cBRF import rbf_network
# cBRF -> nama file cython yang telah dicompile
# rbf_network -> nama salah satu fungsi dalam program cython tersebut
```

Langkah selanjutnya yaitu membandingkan waktu eksekusi dari program yang menggunakan pure native python dengan program cython yang telah dicompile tadi. Dalam proses perbandingan ini menggunakan Jupyter Notebook (IPython). 

![console](https://github.com/agungdwiprasetyo/cython-vs-python/raw/master/pic/console.png)

Dapat dilihat pada line pertama menggunakan pure native python yang eksekusi programnya memakan waktu selama 11.3 sekon. Sedangkan pada program yang menggunakan cython pada line kedua waktu eksekusinya jauh lebih singkat yaitu 101 milisekon. Sungguh peningkatan performa yang cukup signifikan.
