# --- Calculando la Probabilidad de un Evento --- #
# P = Probabilidad
# P(evento) = número de resultados favorables / número de resultados posibles
# rf = Resultados favorables(Lo esperado) | rp = resultados posibles(posibilidades)

def p(a,b):    
    return a/b

if __name__ == '__main__':
    rf = int(input('¿Cuál es el resultado qué esperas? '))
    rp = int(input('¿Cuáles son los resultados posibles? '))
    res=p(rf,rp)
    print(f'La probabilidad es: {res}')
