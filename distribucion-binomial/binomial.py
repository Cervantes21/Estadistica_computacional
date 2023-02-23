import os
# --- Coeficiente Binomial(nCr) --- #
def ncr(a, b):
    ## --- Calculadora Factorial --- ##
    def f(n):
        if n <= 1:
            return n
        else:
            return n * f(n - 1)
    
    ### --- Variables factoriales --- ###
    c = a - b
    fac_a = f(a)
    fac_b = f(b)
    fac_c = f(c)
    
    ### --- Fórmula --- ###
    return fac_a / (fac_b * fac_c)

## ----------------------------- ##
# EntryPoint:
if __name__ == '__main__':
    while True:
        z = input('Presiona Enter para continuar \n Presiona Z para salir ')
        os.system('clear')
        if z.lower() == 'z':
            break
        
        a = int(input('Dame un número A: '))
        b = int(input('Dame un número B: '))
        res = ncr(a, b)
        os.system('clear')
        print(f'El coeficiente Binomial es {res}')

