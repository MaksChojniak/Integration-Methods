import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.integrate import quad, trapezoid, simpson

xx = sp.symbols('xx')
expr = 0.5 + sp.sin(xx/sp.pi) + 1#0.1 * ( (xx**4) - (10 * (xx**3)) + 2000 )
f = sp.lambdify(xx, expr)

def metoda_kwadratow(a, b, n):
    x = np.linspace(a, b, n+1)
    h = (b-a)/n
    suma = 0
    for i in range(n):
        suma += f(x[i])
    
    return suma * h


def metoda_trapezow(a, b, n):
    x = np.linspace(a, b, n+1)
    h = (b-a)/n
    suma = (f(a)+f(b))/2  
    for i in range(1, n):
        suma += f(x[i])
    return suma * h


def metoda_simpsona(a, b, n):
    if n % 2 != 0:
        return -1
    
    calka = f(a) + f(b)
    h = (b-a)/n
    suma_4, suma_2 = 0., 0.
    for i in range(1, n, 2):
        x = a + i*h
        suma_4 += f(x)
    for i in range(2, n-1, 2):
        x = a + i*h
        suma_2 += f(x)
    return (h/3.) * (calka + (4.*suma_4) + (2.*suma_2) )



a, b = 1, 10
x = np.linspace(a, b, 500)
y = np.zeros(x.shape[0], dtype=float)
for i in range(x.shape[0]):
    y[i] = f(x[i])

e = 0.1
calka_dokladna = sp.integrate(expr, (xx, a, b))


print()
print(f"{15*'*'} METODA KWADRATOW {15*'*'}")
calka_kwadratow = 0
n = 0
while np.abs(calka_kwadratow - calka_dokladna) / calka_dokladna * 100 > e:
    n+=1
    calka_kwadratow = metoda_kwadratow(a, b, n)
print(f'krok n: {n}')
print(f'calka metoda kwadratow: {calka_kwadratow:.16f}')
print(f'calka dokladna: {calka_dokladna:.16f}')
print(f'roznica: {np.abs(calka_kwadratow-calka_dokladna):.16f}')

# plt.figure(figsize=(8,8))
# plt.plot(x, y, color='blue', label='f(x) = x^4 - 10x^3 + 2000')

# xi = np.linspace(a, b, n+1)
# for i in range(n+1):
#     plt.plot([xi[i], xi[i]], [0, f(xi[i])], color='red')
#     if i > 0:
#         plt.plot([xi[i-1], xi[i]], [f(xi[i-1]), f(xi[i-1])], color='red')
#         plt.fill_between([xi[i-1], xi[i]], [0, 0], [f(xi[i-1]), f(xi[i-1])], color='red', alpha=0.5)

# plt.title("Calkowanie Metoda Kwadratow")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.grid()
# plt.show()





print()
print(f"{15*'*'} METODA TRAPEZOW {15*'*'}")
calka_trapezow = 0
n = 0
while np.abs(calka_trapezow - calka_dokladna) / calka_dokladna * 100 > e:
    n+=1
    calka_trapezow = metoda_trapezow(a, b, n)
print(f'krok n: {n}')
print(f'calka metoda trapezie: {calka_trapezow:.16f}')
print(f'calka dokladna: {calka_dokladna:.16f}')
print(f'roznica: {np.abs(calka_trapezow-calka_dokladna):.16f}')

# plt.figure(figsize=(8,8))
# plt.plot(x, y, color='blue', label='f(x) = x^4 - 10x^3 + 2000')

# xi = np.linspace(a, b, n+1)
# for i in range(n+1):
#     plt.plot([xi[i], xi[i]], [0, f(xi[i])], color='red')
#     if i > 0:
#         plt.plot([xi[i-1], xi[i]], [f(xi[i-1]), f(xi[i])], color='red')
#         plt.fill_between([xi[i-1], xi[i]], [0, 0], [f(xi[i-1]), f(xi[i])], color='red', alpha=0.5)

# plt.title("Calkowanie Metoda Trapezow")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.grid()
# plt.show()

print()
print(f"{15*'*'} METODA SIMPSONA {15*'*'}")
calka_simpsona = 0
n = 0
while np.abs(calka_simpsona - calka_dokladna) / calka_dokladna * 100 > e:
    n+=1
    calka_simpsona = metoda_simpsona(a, b, n)
print(f'krok n: {n}')
print(f'calka metoda trapezie: {calka_simpsona:.16f}')
print(f'calka dokladna: {calka_dokladna:.16f}')
print(f'roznica: {np.abs(calka_simpsona-calka_dokladna):.16f}')

# plt.figure(figsize=(8,8))
# plt.plot(x, y, color='blue', label='f(x) = x^4 - 10x^3 + 2000')

# xi = np.linspace(a, b, n+1)
# for i in range(n+1):
#     plt.plot([xi[i], xi[i]], [0, f(xi[i])], color='red')
#     # if i > 0:
#     #     plt.plot([xi[i-1], xi[i]], [f(xi[i-1]), f(xi[i])], color='red')
#     #     plt.fill_between([xi[i-1], xi[i]], [0, 0], [f(xi[i-1]), f(xi[i])], color='red', alpha=0.5)

# plt.title("Calkowanie Metoda Trapezow")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.grid()
# plt.show()


print()
print()
print(f"{15*'*'} PROWNANIE Z BIBLIOTEKA SCIPY {15*'*'}")

n_list = [2, 10]
for n in n_list:
    print(f'krok n: {n}')
    x = np.linspace(a, b, n + 1)

    calka_trapezow = metoda_trapezow(a, b, n)
    calka_trapezoid = trapezoid(f(x), x=x)
    
    
    print(f'calka metoda trapezie: {calka_trapezow:.14f}')
    print(f'calka przy uzyciu scipy: {calka_trapezoid:.14f}')
    print(f'roznica dla calek metoda trapezow: {np.abs(calka_trapezow-calka_trapezoid):.14f}')

    print()
    calka_simpson = metoda_simpsona(a, b, n)
    calka_scipy = simpson(f(x), x=x)
    
    print(f'calka metoda simpsona: {calka_simpson:.14f}')
    print(f'calka przy uzyciu scipy: {calka_scipy:.14f}')
    print(f'roznica dla calek metoda simspona: {np.abs(calka_simpson-calka_scipy):.14f}')

    print()
    print()