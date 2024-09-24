def es_primo(numero):
    # Verificamos si un numero dado es primo
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def generador_primos():
    numero = 2
    while True:
        if es_primo(numero):
            # Pausa y devuelve 1 primo
            yield numero
        # Seguimos iterando para buscar otro primo
        numero += 1

# Iterador externo para controlar cuantos primos se desean
def obtener_n_primos(n):
    contador = 0
    # Reanuda el generador cada vez que se solicita
    for primo in generador_primos():
        if contador == n:
            # Detenemos despues de obtener 'n' primos
            break
        print(primo)
        contador += 1

# Ejemplo con los primeros 10 primos
obtener_n_primos(15)
