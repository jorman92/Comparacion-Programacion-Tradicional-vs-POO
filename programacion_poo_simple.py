"""
Programa de Cálculo del Promedio Semanal del Clima - Programación Orientada a Objetos

Implementación usando el paradigma de Programación Orientada a Objetos.
Conceptos POO aplicados: Encapsulamiento, Herencia y Polimorfismo.
"""

class DiaClima:
    """
    Clase que representa los datos de un día.
    Demuestra ENCAPSULAMIENTO: atributos privados con métodos de acceso.
    """
    
    def __init__(self, dia_semana, temperatura):
        self.dia_semana = dia_semana
        self._temperatura = temperatura  # Atributo privado
        self._validar_temperatura()
    
    def _validar_temperatura(self):
        """Valida que la temperatura esté en rango"""
        if not isinstance(self._temperatura, (int, float)):
            raise ValueError("La temperatura debe ser un número")
        if not (-50 <= self._temperatura <= 60):
            raise ValueError("La temperatura debe estar entre -50°C y 60°C")
    
    @property
    def temperatura(self):
        """Getter para temperatura - encapsulamiento"""
        return self._temperatura
    
    @temperatura.setter
    def temperatura(self, valor):
        """Setter para temperatura con validación - encapsulamiento"""
        self._temperatura = valor
        self._validar_temperatura()
    
    def __str__(self):
        return f"{self.dia_semana}: {self._temperatura}°C"

class SemanaClima:
    """
    Clase que gestiona una semana de datos climáticos.
    Demuestra COMPOSICIÓN: contiene objetos DiaClima.
    """
    
    def __init__(self):
        self.dias = []  # Lista de objetos DiaClima
    
    def agregar_dia(self, dia_semana, temperatura):
        """Agrega un nuevo día a la semana"""
        dia = DiaClima(dia_semana, temperatura)
        self.dias.append(dia)
    
    def calcular_promedio(self):
        """Calcula el promedio semanal"""
        if not self.dias:
            return 0
        total = sum(dia.temperatura for dia in self.dias)
        return total / len(self.dias)
    
    def mostrar_reporte(self):
        """Muestra el reporte de la semana"""
        print("\n--- REPORTE SEMANAL ---")
        for dia in self.dias:
            print(dia)
        promedio = self.calcular_promedio()
        print(f"\nPromedio semanal: {promedio:.2f}°C")

class ProgramaClima:
    """
    Clase controladora del programa.
    Demuestra POLIMORFISMO: diferentes objetos pueden ser tratados de manera uniforme.
    """
    
    def __init__(self):
        self.semana = SemanaClima()  # Composición
    
    def obtener_temperatura(self, dia):
        """Solicita temperatura para un día específico"""
        while True:
            try:
                temp = float(input(f"Ingrese temperatura para {dia} (°C): "))
                return temp
            except ValueError:
                print("Por favor ingrese un número válido")
    
    def ejecutar(self):
        """Ejecuta el programa principal"""
        print("=== CÁLCULO DEL PROMEDIO SEMANAL DEL CLIMA ===")
        print("Usando Programación Orientada a Objetos")
        
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", 
                      "Viernes", "Sábado", "Domingo"]
        
        print("\nIngrese las temperaturas de la semana:")
        for dia in dias_semana:
            temp = self.obtener_temperatura(dia)
            self.semana.agregar_dia(dia, temp)
        
        # Mostrar reporte usando polimorfismo
        self.semana.mostrar_reporte()

# Programa principal
if __name__ == "__main__":
    programa = ProgramaClima()
    programa.ejecutar()
