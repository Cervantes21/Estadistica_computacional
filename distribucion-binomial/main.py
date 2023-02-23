import os
# Importamos nuestras funciones modulares.
from binomial import ncr
from no_probabilidad import q
from probabilidad import p

# --- Distribución Binomial --- #
## Formúla: p(x)= (n nrc x)* p**2 * q**(n - x)
def d_bim(x,n,a,b):
    prob = p(a, b)
    q_prob = q(1 - prob, a, b)
    coef_bin=ncr(n, x)
    return coef_bin * prob**x * q_prob**(n - x)

# Entrypoint:
if __name__ == '__main__':
    # Probabilidad
    rf = int(input('¿Cuál es tu resultado favorable? '))
    rp = int(input('¿Cuáles son los resultados posibles? '))
    res_prob = p(rf, rp)
    print(f'La probabilidad es: {res_prob}')

    # No probabilidad
    a = rf
    b = rp
    evento = res_prob 
    no_prob = q(1 - evento, a, b)
    print(f'La probabilidad de que no ocurra es: {no_prob}')

    # Coeficiente binomial
    coef_res = ncr(b, rf)
    print(f'El coeficiente Binomial es {coef_res}')

    # Distribución Binomial
    x = int(input('Probabilidad a calcular: '))
    n = int(input('Tamaño total de la muestra: '))
    dist_bim = d_bim(x, n, a, b)
    print(f'La distribución Binomial es de {dist_bim} en porcentaje es: {dist_bim * 100}')

