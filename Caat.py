# Herramienta de Auditoría Asistida por Computadora (CAAT)
# Autor: Veronica Chicaiza
# Fecha: 23/01/2025
# Descripción: Esta herramienta realiza pruebas de auditoría sobre un conjunto de datos predefinido.

"""
   Muestra el menú de opciones disponibles para el usuario.
"""

def mostrar_menu():
    print("\n--- Herramienta de Auditoría Asistida por Computadora (CAAT) ---")
    print("1. Prueba de duplicados")
    print("2. Prueba de anomalías")
    print("3. Prueba de formato")
    print("4. Prueba de cumplimiento")
    print("5. Prueba de auditoría horaria")
    print("0. Salir")

"""
    Realiza una prueba de duplicados en los datos.
"""

def prueba_duplicados(datos):
    print("Ejecutando prueba de duplicados...")
    duplicados = [item for item in datos if datos.count(item) > 1]
    if duplicados:
        print(f"Elementos duplicados encontrados: {set(duplicados)}")
    else:
        print("No se encontraron elementos duplicados.")

"""
    Realiza una prueba de anomalías en los datos.
"""

def prueba_anomalias(datos):
    print("Ejecutando prueba de anomalías...")
    umbral = 10000  # Valor de referencia para detectar anomalías
    anomalias = [item for item in datos if item > umbral]
    if anomalias:
        print(f"Anomalías detectadas: {anomalias}")
    else:
        print("No se detectaron anomalías.")

"""
    Realiza una prueba de formato en los datos.
"""

def prueba_formato(datos):
    print("Ejecutando prueba de formato...")
    formato_correcto = lambda x: x.startswith("EMP-") and x[4:].isdigit()
    incorrectos = [item for item in datos if not formato_correcto(item)]
    if incorrectos:
        print(f"Datos con formato incorrecto: {incorrectos}")
    else:
        print("Todos los datos tienen el formato correcto.")

"""
    Realiza una prueba de cumplimiento en los datos.
"""

def prueba_cumplimiento(datos):
    print("Ejecutando prueba de cumplimiento...")
    requisitos = ["Producto-A", "Producto-B", "Producto-C"]  # Elementos requeridos
    faltantes = [req for req in requisitos if req not in datos]
    if faltantes:
        print(f"Elementos faltantes para el cumplimiento: {faltantes}")
    else:
        print("Todos los requisitos de cumplimiento están presentes.")

"""
    Realiza una prueba de auditoría horaria en los datos.
"""

def prueba_horaria(datos):
    print("Ejecutando prueba de auditoría horaria...")
    horarios_invalidos = [hora for hora in datos if not (0 <= hora <= 23)]
    if horarios_invalidos:
        print(f"Horarios inválidos encontrados: {horarios_invalidos}")
    else:
        print("Todos los horarios son válidos.")

"""
    Ejecuta la prueba seleccionada por el usuario.
"""

def ejecutar_prueba(opcion, datos_duplicados, datos_anomalias, datos_formato, datos_cumplimiento, datos_horaria):
    if opcion == "1":
        prueba_duplicados(datos_duplicados)
    elif opcion == "2":
        prueba_anomalias(datos_anomalias)
    elif opcion == "3":
        prueba_formato(datos_formato)
    elif opcion == "4":
        prueba_cumplimiento(datos_cumplimiento)
    elif opcion == "5":
        prueba_horaria(datos_horaria)
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")

"""
    Función principal que ejecuta la herramienta de auditoría.
"""

def main():
    # Datos de prueba separados por categoría
    datos_duplicados = ["Factura-001", "Factura-002", "Factura-003", "Factura-001"]  # Duplicados
    datos_anomalias = [1500.50, 200.75, 5000.00, 100000.00]  # Anomalías (montos de transacciones)
    datos_formato = ["EMP-001", "EMP-002", "EMP-003", "EMP-ABC", "EMP123", "ABC-001"]  # Formato (códigos de empleados)
    datos_cumplimiento = ["Producto-A", "Producto-B", "Producto-C", "Producto-X"]  # Cumplimiento (productos)
    datos_horaria = [8, 9, 10, 25, -1, 15.5]  # Auditoría horaria (horas)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "0":
            print("Saliendo de la herramienta. ¡Hasta pronto!")
            break
        ejecutar_prueba(opcion, datos_duplicados, datos_anomalias, datos_formato, datos_cumplimiento, datos_horaria)

if __name__ == "__main__":
    main()