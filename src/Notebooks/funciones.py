def clean_value(value):
    # Reemplazar comas por puntos
    value = value.replace(',', '.')

    # Eliminar todo lo que sigue después del segundo punto (.)
    if value.count('.') > 1:
        value = value.rsplit('.', 1)[0]

    return float(value)