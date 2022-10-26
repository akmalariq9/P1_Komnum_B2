# P1_Komnum_B2
**Repositoy untuk Praktikum 1 Komputasi Numerik ( B ) - Kelompok 2**
## **Anggota Kelompok**
| Nama                     | NRP        | Kelas    |
| -------------------------| -----------| ---------|
| Alfan Lukeyan Rizki      | 5025211046 | Komnum B |
| Akmal Ariq Romadhon      | 5025211188 | Komnum B |
| Muhammad Rifqi Fadhillah | 5025211228 | Komnum B |

## **Soal Praktikum**
> Anda sudah mengerti algoritma pemrosesan metode Bolzano, dan anda sudah memahami cara kerjanya. Sekarang anda tinggal mengimplementasikan algoritma tersebut menjadi sebuah program komputer metode Bolzano (yang dapat menampilkan proses iteratif numerik, lengkap dengan grafik fungsinya).

## **Jawaban**
Metode Bolzano atau dapat juga disebut metode setengah interval (Interval Halving), merupakan salah satu metode yang dapat digunakan dalam mencari akar akar dari sebuah persamaan. Terdapat beberapa aplikasi yang bisa digunakan untuk mengimplementasikan Metode Bolzano, seperti google spreadsheets. Namun disini, akan digunakan bahasa python dalam implementasi Metode Bolzano. Berikut adalah code yang digunakan untuk implementasi Metode Bolzano, sekaligus jawaban dari Soal Praktikum 1 Komputasi Numerik. <br>  
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
        result = ( b + a ) / 2
    print(tabulate(data, headers = "firstrow", tablefmt = "pretty"))
    print(f"Batas Bawah : {a}")
    print(f"Batas Atas : {b}")
    print(f"Akar setelah iterasi ke - {loop} adalah {result}")
    return result
```
Dalam fungsi tersebut, `def f(x)` digunakan untuk menjalankan perintah dari variabel `function input` sesuai syntax bahasa python. Salah satu contohnya adalah ketika persamaan yang digunakan ialah $x^3$, maka dalam proses input menjadi `x**3` sesuai syntax dari python. Kemudian dibuat tabel yang berisi `iterasi`, `x1`, `x2`, `x3`, `f(x1)`, `f(x2)`, dan `f(x3)`. Selanjutnya, digunakan looping sesuai jumlah iterasi yang diinginkan. Apabila `f(c) * f(b) < 0`, maka `a = c`. Selain itu, apabila `f(c) * f(a) < 0`, maka `b = c`. Setelah itu, didapatkan nilai x yang baru, dari rumus `b + a / 2` sesuai dengan Teori Bolzano. Perintah selanjutnya ialah print atau menampilkan hasil dari perhitungan yang sudah dilakukan. <br>

Setelah proses perhitungan atau pembuatan fungsi dari Metode Bolzano selesai, maka langkah selanjutnya adalah penyesuaian dengan program. Contohnya ialah memasukkan input, print output, penyesuaian variabel, dan sebagainya. Berikut adalah code yang digunakan dalam proses tersebut :
```python
if __name__ == "__main__" :
    function = input("Fungsi : ")
    a = float(input("Batas Bawah : "))
    b = float(input("Batas Atas : "))
    loop = int(input("Jumlah Iterasi : "))

    x = np.linspace(0,5, num = 1000)
    y = eval(function)

    def f(x):
        f = eval(function)
        return f
    result = bisection(function, a, b, loop)

    plt.plot(x, y)
    plt.axhline(0, -10, 10, color='black', linewidth=1)
    plt.axvline(0, min(y), max(y), color='black', linewidth=1)
    plt.scatter(result, f(result), color='C1', linewidth=4)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
```
Dalam code tersebut, hal yang dilakukan adalah deklarasi variabel `function`, `a`, `b`, dan `loop` atau `iterasi`. Keempat variabel tersebut berasal dari input user, dengan tipe data `float` untuk variabel `a` dan `b`, serta `integer` untuk variabel `loop`. Nilai `x` didapat menggunakan fungsi `linspace` dari library `numpy` dan `y` berasal dari proses perhitungan. Kemudian digunakan juga bantuan dari library `matplotlib` yang telah diinput dengan nama `plt` untuk membuat grafik. Fungsi yang melibatkan matplotlib diantaranya ialah scatter untuk membuat titik, plot untuk membuat grafik, dan show untuk menampilkan grafik. Berikut adalah contoh jalannya program Metode Bolzano dengan input $x^2 - 10$, $a = -2,$ dan $b = 5$
<br>

**Menggunakan Calculator Online**
![a1](https://user-images.githubusercontent.com/109916703/198058653-8a9d91c3-7320-4ad4-b1f3-2fb942c020e1.png)

**Menggunakan Program Metode Bolzano**
![a2](https://user-images.githubusercontent.com/109916703/198060078-885a732f-990b-4c87-aa5b-e588b2159386.png)

**Grafik yang Dihasilkan**

![a3](https://user-images.githubusercontent.com/109916703/198060873-374ac42b-ff26-4299-864b-d359dafd4b1e.png)


# End Of The Line.
```c
#include <stdio.h>

int main(){
    printf("Thank u!");
}
```
