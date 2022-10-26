# P1_Komnum_B2
Repositoy untuk Praktikum 1 Komputasi Numerik ( B ) - Kelompok 2
## **Anggota Kelompok**
| Nama                     | NRP        | Kelas    |
| -------------------------| -----------| ---------|
| Alfan Lukeyan Rizki      | 5025211046 | Komnum B |
| Akmal Ariq Romadhon      | 5025211188 | Komnum B |
| Muhammad Rifqi Fadhillah | 5025211228 | Komnum B |

## **Soal Praktikum**
> Anda sudah mengerti algoritma pemrosesan metode Bolzano, dan anda sudah memahami cara kerjanya. Sekarang anda tinggal mengimplementasikan algoritma tersebut menjadi sebuah program komputer metode Bolzano (yang dapat menampilkan proses iteratif numerik, lengkap dengan grafik fungsinya).

## **Jawaban**
Metode Bolzano atau dapat juga disebut metode setengah interval (Interval Halving), merupakan salah satu metode yang dapat digunakan dalam mencari akar akar dari sebuah persamaan. Terdapat beberapa aplikasi yang bisa digunakan untuk mengimplementasikan Metode Bolzano, seperti google spreadsheets. Namun disini, akan digunakan bahasa python dalam implementasi Metode Bolzano. Berikut adalah code yang digunakan untuk implementasi Metode Bolzano, sekaligus jawaban dari Soal Praktikum 1 Komputasi Numerik.<br>
<br>
Sebelum memulai semuanya, maka langkah pertama yang harus dilakukan adalah dengan install beberapa library seperti `matplotlib`, `tabulate`, dan `numpy`. Setelah itu, maka harus dilakukan import kedalam project dengan cara sebagai berikut :<br>
```python
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
```
Kemudian pengerjaan dilanjutkan dengan membuat `fungsi bisection` yang akan digunakan dalam proses pencarian akar menggunakan Metode Bolzano. Berikut adalah code yang digunakan :
```python
def bisection(functioninput, a, b, loop):
    i = 1
    def f(x):
        f = eval(functioninput)
        return f
    
    data = [['iterasi','x1', 'x2', 'x3', 'f(x1)', 'f(x2)', 'f(x3)']]
    for i in range(loop):
        c = ( b + a ) / 2
        data.append([i, a, b, c, f(a), f(b), f(c)])
        i = i + 1
        if f(c) * f(b) < 0:
            a = c
        elif f(c) * f(a) < 0:
            b = c
        ans = ( b + a ) / 2
    print(tabulate(data, headers = "firstrow", tablefmt = "pretty"))
    print(f"Batas Bawah : {a}")
    print(f"Batas Atas : {b}")
    print(f"Akar setelah iterasi ke - {loop} adalah {ans}")
    return ans
```
Dalam fungsi tersebut, `def f(x)` digunakan untuk menjalankan perintah dari variabel `function input` sesuai syntax bahasa python. Salah satu contohnya adalah ketika persamaan yang digunakan ialah $x^3$, maka dalam proses input menjadi `x**3` sesuai syntax dari python. Kemudian dibuat tabel yang berisi `iterasi`, `x1`, `x2`, `x3`, `f(x1)`, `f(x2)`, dan `f(x3)`. Selanjutnya, digunakan looping sesuai jumlah iterasi yang diinginkan. Apabila `f(c) * f(b) < 0`, maka `a = c`. Selain itu, apabila `f(c) * f(a) < 0`, maka `b = c`. Setelah itu, didapatkan nilai x yang baru, dari rumus `b + a / 2` sesuai dengan Teori Bolzano.
