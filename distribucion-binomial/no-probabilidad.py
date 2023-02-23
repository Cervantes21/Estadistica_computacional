import os
# Importamos nuestra función de probabilidad.
from probabilidad import p 

# --- No probabilidad --- #
# Q = P(no evento) = 1 - P(evento)

def q(x):
    x = p(a,b)
    return 1 - x

if __name__ == '__main__':
    
    a = int(input('Dame un número A: '))
    b = int(input('Dame un número B: '))
    os.system('clear')
    evento=p(a,b)
    no_prob=q(evento)
    print(f'La probabilidad de que no ocurra es: {no_prob}')
    


