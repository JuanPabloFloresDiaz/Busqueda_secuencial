"""
Sistema de Control de Asistencia de Estudiantes
Utiliza búsqueda secuencial para verificar la presencia de estudiantes en clase.
Permite buscar, agregar estudiantes y mostrar estadísticas de búsqueda.
"""

from Teclado import Teclado
from BubbleSort import bubble_sort

class ControlAsistencia:
    def __init__(self):
        # Lista inicial con 10 nombres de estudiantes
        self.estudiantes = [
            "Ana García",
            "Carlos López",
            "María Rodríguez",
            "José Martínez",
            "Laura Hernández",
            "David Pérez",
            "Carmen Jiménez",
            "Roberto Silva",
            "Patricia Morales",
            "Fernando Castro"
        ]
        
        # Contadores de búsquedas
        self.busquedas_fallidas = 0
        self.conteo_busquedas = {}  # Diccionario para contar búsquedas por estudiante
    
    def busqueda_secuencial(self, nombre_buscado):
        """
        Realiza búsqueda secuencial en la lista de estudiantes.
        La búsqueda es case-insensitive.
        
        Args:
            nombre_buscado (str): Nombre del estudiante a buscar
            
        Returns:
            tuple: (encontrado: bool, posicion: int or -1)
        """
        nombre_buscado = nombre_buscado.strip().lower()
        
        for i, estudiante in enumerate(self.estudiantes):
            if estudiante.lower() == nombre_buscado:
                return True, i
        
        return False, -1
    
    def contar_busqueda(self, nombre):
        """
        Cuenta las veces que se ha buscado cada estudiante.
        
        Args:
            nombre (str): Nombre del estudiante buscado
        """
        nombre_normalizado = nombre.strip().title()
        if nombre_normalizado in self.conteo_busquedas:
            self.conteo_busquedas[nombre_normalizado] += 1
        else:
            self.conteo_busquedas[nombre_normalizado] = 1
    
    def agregar_estudiante(self, nombre):
        """
        Agrega un nuevo estudiante a la lista.
        
        Args:
            nombre (str): Nombre del estudiante a agregar
        """
        nombre_formateado = nombre.strip().title()
        if nombre_formateado not in [est.title() for est in self.estudiantes]:
            self.estudiantes.append(nombre_formateado)
            print(f"✓ Estudiante '{nombre_formateado}' agregado a la lista.")
        else:
            print(f"⚠ El estudiante '{nombre_formateado}' ya está en la lista.")
    
    def mostrar_lista_estudiantes(self):
        """Muestra la lista actual de estudiantes ordenada alfabéticamente."""
        print("\n" + "="*50)
        print("📋 LISTA ACTUAL DE ESTUDIANTES")
        print("="*50)
        
        # Ordenar la lista usando el módulo BubbleSort
        estudiantes_ordenados = bubble_sort(self.estudiantes.copy(), key=str.lower)
        
        for i, estudiante in enumerate(estudiantes_ordenados, 1):
            print(f"{i:2d}. {estudiante}")
        print(f"\nTotal de estudiantes: {len(self.estudiantes)}")
    
    def mostrar_estadisticas(self):
        """Muestra las estadísticas de búsquedas realizadas."""
        print("\n" + "="*60)
        print("📊 ESTADÍSTICAS DE BÚSQUEDAS")
        print("="*60)
        print(f"Total de búsquedas fallidas: {self.busquedas_fallidas}")
        
        if self.conteo_busquedas:
            print("\nConteo de búsquedas por estudiante:")
            print("-" * 40)
            
            # Ordenar el diccionario por nombre
            estudiantes_buscados = sorted(self.conteo_busquedas.items())
            
            for nombre, cantidad in estudiantes_buscados:
                print(f"{nombre}: {cantidad} búsqueda(s)")
        else:
            print("No se realizaron búsquedas durante esta sesión.")
    
    def buscar_estudiante(self):
        """Proceso principal de búsqueda de estudiantes."""
        while True:
            print("\n" + "-"*50)
            nombre = Teclado.read_text(
                "Ingresa el nombre del estudiante a buscar (o 'salir' para terminar):",
                min_length=1
            )
            
            # Verificar si el usuario quiere salir
            if nombre.lower() == 'salir':
                break
            
            # Contar la búsqueda
            self.contar_busqueda(nombre)
            
            # Realizar búsqueda secuencial
            encontrado, posicion = self.busqueda_secuencial(nombre)
            
            if encontrado:
                print(f"✅ Estudiante '{self.estudiantes[posicion]}' estuvo presente.")
            else:
                print(f"❌ Estudiante '{nombre.title()}' no asistió a la clase.")
                self.busquedas_fallidas += 1
                
                # Preguntar si desea agregar el estudiante
                respuesta = Teclado.read_text(
                    "¿Deseas agregar este estudiante a la lista? (s/n):",
                    min_length=1,
                    max_length=1
                ).lower()
                
                if respuesta == 's':
                    self.agregar_estudiante(nombre)
    
    def ejecutar(self):
        """Método principal que ejecuta el sistema de control de asistencia."""
        print("=" * 60)
        print("🎓 SISTEMA DE CONTROL DE ASISTENCIA DE ESTUDIANTES")
        print("=" * 60)
        print("Este sistema permite verificar la asistencia de estudiantes usando búsqueda secuencial.")
        
        while True:
            print("\n" + "="*50)
            print("📚 MENÚ PRINCIPAL")
            print("="*50)
            print("1. Ver lista de estudiantes")
            print("2. Buscar estudiantes")
            print("3. Agregar estudiante manualmente")
            print("4. Ver estadísticas")
            print("5. Salir")
            
            opcion = Teclado.read_integer(
                "Selecciona una opción:",
                min_value=1,
                max_value=5
            )
            
            if opcion == 1:
                self.mostrar_lista_estudiantes()
            elif opcion == 2:
                self.buscar_estudiante()
            elif opcion == 3:
                nombre = Teclado.read_text(
                    "Ingresa el nombre del estudiante a agregar:",
                    min_length=2,
                    max_length=50
                )
                self.agregar_estudiante(nombre)
            elif opcion == 4:
                self.mostrar_estadisticas()
            elif opcion == 5:
                print("\n🎯 RESUMEN FINAL:")
                self.mostrar_estadisticas()
                print("\n¡Gracias por usar el sistema de control de asistencia!")
                break

def main():
    """Función principal del programa."""
    try:
        sistema = ControlAsistencia()
        sistema.ejecutar()
    except KeyboardInterrupt:
        print("\n\n⚠ Programa interrumpido por el usuario.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("Por favor, contacta al administrador del sistema.")

if __name__ == "__main__":
    main()
