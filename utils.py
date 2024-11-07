def wrap_text(text, font, max_width):
    """
    Función para ajustar el texto dentro de un ancho máximo.
    Devuelve una lista de líneas de texto ajustadas.
    """
    words = text.split(' ')
    lines = []
    current_line = ''
    for word in words:
        # Verifica si la palabra cabe en la línea actual
        test_line = current_line + ' ' + word if current_line else word
        test_width = font.size(test_line)[0]
        if test_width <= max_width:
            current_line = test_line
        else:
            # Si la palabra no cabe, agregamos la línea actual y empezamos una nueva
            lines.append(current_line)
            current_line = word
    lines.append(current_line)  # Añadir la última línea
    return lines