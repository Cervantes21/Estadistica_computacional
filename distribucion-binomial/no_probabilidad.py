import os
# Importamos nuestra función de probabilidad.
from probabilidad import p 

# --- No probabilidad --- #
# Q = 'Que no ocurra un evento'
# Formula: P(no evento) = 1 - P(evento)

def q(x,a,b):
    p_evento = p(a,b)
    return 1 - p_evento

if __name__ == '__main__':
    
    a = int(input('Dame un número A: '))
    b = int(input('Dame un número B: '))
    os.system('clear')
    evento=p(a,b)
    x = evento
    no_prob=q(x,a,b)
    print(f'La probabilidad de que no ocurra es: {no_prob}')
    


