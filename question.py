import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': list(p.preguntas_basicas.keys()),
            'intermedias': list(p.preguntas_intermedias.keys()),
            'avanzadas': list(p.preguntas_avanzadas.keys())}
###############################################

def choose_q(dificultad):
    # Escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]

    # Usar opciones desde ambiente global
    global opciones

    # Escoger una pregunta aleatoriamente 
    n_elegido = random.choice(opciones[dificultad])
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)

    # Escoger enunciado y alternativas mezcladas
    pregunta = preguntas[n_elegido]
    alternativas_mezcladas = shuffle_alt(pregunta)  
    return pregunta['enunciado'], alternativas_mezcladas

if __name__ == '__main__':
    # Si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    