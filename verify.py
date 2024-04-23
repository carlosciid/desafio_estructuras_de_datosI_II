import preguntas as p


def verificar(alternativas, eleccion):
    # Convierte la elección (a, b, c, d) en un índice numérico (0, 1, 2, 3)
    eleccion_idx = ['a', 'b', 'c', 'd'].index(eleccion)

    # Encontrar el índice de la alternativa correcta
    correcto_idx = next(i for i, alt in enumerate(alternativas) if alt[1] == 1)

    # Verificar si la elección es correcta comparando los índices
    correcto = eleccion_idx == correcto_idx

    # Imprime el resultado de la verificación
    if correcto:
        print("Respuesta correcta!")
    else:
        print("Respuesta incorrecta.")

    return correcto

if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Simulando el módulo preguntas y un ejemplo de ejecución
    # Asumiendo que 'p.pool_preguntas' y la función 'print_pregunta' están correctamente definidos
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)
