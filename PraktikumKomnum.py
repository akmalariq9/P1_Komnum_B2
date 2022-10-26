import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

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