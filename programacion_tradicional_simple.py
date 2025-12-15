"""""""""""""""""""""""Programa de Cálculo del Promedio Semanal del Clima - Programación Orientada a Objetos
Fecha: 2025-12-14
Este programa utiliza el paradigma de Programación Orientada a Objetos (POO)
para calcular el promedio semanal de temperaturas, implementando encapsulamiento,
herencia y polimorfismo.
"""

def obtener_temperatura():

    """Solicita y retorna una temperatura válida"""

    while True:
        try:
            temp = float(input("Ingrese la temperatura (°C): "))
            if -50 <= temp <= 60:
                return temp
            else:
                print("Temperatura debe estar entre -50°C y 60°C")
        except ValueError:
            print("Por favor ingrese un número válido")

def calcular_promedio(temperaturas):

    """Calcula el promedio de una lista de temperaturas"""
    return sum(temperaturas) / len(temperaturas)

def mostrar_resultados(temperaturas, promedio):

    """Muestra los resultados del cálculo"""
    print("\n--- RESULTADOS ---")
    for i, temp in enumerate(temperaturas):
        dia = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"][i]
        print(f"{dia}: {temp}°C")
    
    print(f"\nPromedio semanal: {promedio:.2f}°C")

def main():

    """Función principal que coordina el programa"""
    
    print("=== CÁLCULO DEL PROMEDIO SEMANAL DEL CLIMA ===")
    print("Usando Programación Tradicional")
    
    # Lista para almacenar las temperaturas
    temperaturas = []
    
    print("\nIngrese las temperaturas de la semana:")
    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
        print(f"\n{dia}:")
        temp = obtener_temperatura()
        temperaturas.append(temp)
    
    # Calcular promedio
    promedio = calcular_promedio(temperaturas)
    
    # Mostrar resultados
    mostrar_resultados(temperaturas, promedio)

if __name__ == "__main__":
    main()
"""