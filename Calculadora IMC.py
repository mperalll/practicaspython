

    # Psicoeducación sobre el IMC
print("El índice de masa corporal (IMC) sirve para medir la relación entre el peso y la talla, lo que permite identificar el sobrepeso y la obesidad en adultos. Se calcula dividiendo el peso (en kilogramos) entre la estatura (en metros).")
print("Al realizar esta operación, el resultado es el IMC, el cual se clasifica de la siguiente manera:")
print("""
      Menor a 18.9   = peso bajo
      18.50 a 24.99  = peso normal
      25.00 a 29.99  = sobrepeso
      30.00 a 34.99  = obesidad leve
      35.00 a 39.99  = obesidad media
      Mayor a 40.0   = obesidad mórbida
""")

# Validaciones
def validar_edad(edad):
    return edad.isdigit() and int(edad) > 0

def validar_numero_decimal(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False

# Pedimos la cantidad de personas
while True:
    try:
        personas = int(input("Número de personas: "))
        if personas > 0:
            break
        else:
            print("Debe ingresar un número mayor a 0.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Proceso para cada persona
while personas > 0:
    # Solicitar nombre
    nombre = input("¿Cómo te llamas? ")

    # Solicitar edad con validación
    while True:
        edad = input("¿Cuántos años tienes? Ingresa sólo el número: ")
        if validar_edad(edad):
            edad = int(edad)
            break
        else:
            print("Por favor, ingresa una edad válida en números enteros.")

    # Solicitar peso con validación
    while True:
        peso = input("¿Cuánto pesas? Ingresa tu peso en KG: ")
        if validar_numero_decimal(peso):
            peso = float(peso)
            break
        else:
            print("Por favor, ingresa un peso válido en formato decimal.")

    # Solicitar altura con validación
    while True:
        altura = input("¿Cuánto mides? Ingresa tu altura en metros: ")
        if validar_numero_decimal(altura):
            altura = float(altura)
            break
        else:
            print("Por favor, ingresa una altura válida en formato decimal.")

    # Calcular el IMC
    IMC = peso / altura ** 2

    # Mostrar el valor del IMC
    print(f"{nombre}, su IMC es de {IMC:.2f}")

    # Clasificación según el IMC
    if IMC <= 15.99:
        print("Delgadez severa")
    elif IMC <= 16.99:
        print("Delgadez moderada")
    elif IMC <= 18.49:
        print("Delgadez leve")
    elif IMC <= 24.99:
        print("Peso normal")
    elif IMC <= 29.99:
        print("Sobrepeso")
    elif IMC <= 34.99:
        print("Obesidad leve")
    elif IMC <= 39.99:
        print("Obesidad media")
    else:
        print("Obesidad mórbida")

    # Indicaciones según el resultado
    if IMC <= 18.49:
        print(f"Estás muy delgado, {nombre}. A tu edad de {edad} años deberías comer más.")
    elif IMC <= 26.99:
        print(f"Tu masa corporal es normal, {nombre}. A tu edad de {edad} años estás en óptimas condiciones.")
    elif IMC <= 30.99:
        print(f"Estás engordando, {nombre}. A tu edad de {edad} años ya tienes obesidad.")
    elif IMC <= 35.99:
        print(f"{nombre}, a tu edad de {edad} años estás bastante obeso. Debes hacer ejercicio.")
    else:
        print(f"{nombre}, a tu edad de {edad} años tienes obesidad mórbida. Debes tener mucho cuidado y empezar a cuidarte.")

    # Restamos una persona al contador
    personas -= 1
