import csv

# Definir una clase para representar libros
class Libro:
    def __init__(self, titulo, autor, fecha, sede, codigo, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.fecha = fecha
        self.sede = sede
        self.codigo = codigo
        self.disponible = disponible

# Definir una clase para la biblioteca
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sedes = {}

    def agregar_libro(self, libro):
        if libro.sede in self.sedes:
            self.sedes[libro.sede].append(libro)
        else:
            self.sedes[libro.sede] = [libro]

    def listar_libros(self, sede=None):
        if sede:
            if sede in self.sedes:
                print(f"Libros disponibles en la sede '{sede}' de la biblioteca:")
                for libro in self.sedes[sede]:
                    estado = "Disponible" if libro.disponible else "No Disponible"
                    print(f"{libro.titulo} - {libro.autor} ({libro.fecha}) - {estado} - {libro.codigo}")
            else:
                print(f"No existe la sede '{sede}' en la biblioteca.")
        else:
            print("Debes especificar una sede para listar los libros.")

    def buscar_libro(self, codigo, sede):
        if sede in self.sedes:
            for libro in self.sedes[sede]:
                if libro.codigo == codigo:
                    return libro
        return None

    def alquilar_libro(self, usuario_codigo, usuario_nombre, codigo_libro, sede):
        libro = self.buscar_libro(codigo_libro, sede)
        if libro:
            if libro.disponible:
                libro.disponible = False
                print(f"{usuario_nombre} ha alquilado '{libro.titulo}' con codigo '{codigo_libro}' en la sede '{sede}'")
            else:
                print(f"'{libro.titulo}' no está disponible actualmente en la sede '{sede}'.")
        else:
            print(f"'{codigo_libro}' no se encuentra en la sede '{sede}' de la biblioteca.")



# Función para cargar libros desde un archivo CSV
def cargar_libros_desde_archivo(archivo):
    with open(archivo, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            libro = Libro(row['Titulo'], row['Autor'], row['Fecha'], row['Sede'], row['Codigo'])
            biblioteca.agregar_libro(libro)

# Crear una instancia de la biblioteca
biblioteca = Biblioteca("Biblioteca Universitaria")

# Cargar libros desde un archivo CSV (reemplaza 'libros.csv' con tu archivo)
cargar_libros_desde_archivo('libros.csv')

# Mostrar las sedes disponibles al usuario
print("Sedes disponibles:")
for sede in biblioteca.sedes.keys():
    print(sede)

# Solicitar al usuario la sede donde desea buscar libros
sede = input("Ingresa la sede donde deseas buscar libros: ")

# Listar libros disponibles en la sede seleccionada
biblioteca.listar_libros(sede)

# Solicitar al usuario el título del libro que desea alquilar
codigo_libro = input("Ingresa el codigo del libro que deseas alquilar: ")

# Alquilar el libro en la sede seleccionada
usuario_codigo = input("Ingresa tu código de usuario: ")
usuario_nombre = input("Ingresa tu nombre: ")
biblioteca.alquilar_libro(usuario_codigo, usuario_nombre, codigo_libro, sede)
