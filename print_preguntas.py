import preguntas as p

def print_pregunta(enunciado, alternativas):
    # Imprimir enunciado y alternativas
    print(enunciado[0])  # Assuming enunciado is a list with one item
    letras = ['A', 'B', 'C', 'D']
    for i, alt in enumerate(alternativas):
        print(f"{letras[i]}. {alt[0]}")

if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    
    # Expected output:
    # Enunciado básico 1
    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4
