def choose_level(n_pregunta, p_level):
    if p_level == 1:
        # Si sólo hay una pregunta por nivel, todo se considera básico para simplificar.
        level = 'basicas'
    elif p_level == 2:
        if n_pregunta <= 2:
            level = 'basicas'
        elif n_pregunta <= 4:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    elif p_level == 3:
        if n_pregunta <= 3:
            level = 'basicas'
        elif n_pregunta <= 6:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    else:
        # Si p_level tiene un valor inesperado, establecemos un valor predeterminado
        # Podrías elegir manejar este caso de error de manera diferente si lo prefieres
        level = 'basicas'
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 1)) # básicas, dado que el valor máximo de preguntas no se maneja
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias
