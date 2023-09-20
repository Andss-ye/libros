import json

def split_linea(linea):
        valores = linea.split()

        if len(valores) > 5:
            valores = valores[:5]

        return valores

class Libro():
    def __init__(self):
        f = open("libros.txt", "r")
        libros = []
        for linea in f:
            libro = json.loads(linea)
            libros.append(libro)
        f.close()

    def prestar_libro(self):
        codigo_libro = input("Introduce el código del libro que deseas coger: ")

        with open("libros.txt", "r") as f:
            for linea in f:
                libro = json.loads(linea)
                if libro["codigo"] == codigo_libro:
                    print(f"Se ha prestado el libro {libro['titulo']}")
                    return True
            else:
                print("El libro no existe.")
                return False


    def devolver_libro(self):
        codigo_libro = input("Introduce el código del libro que deseas devolver: ")

        with open("libros.txt", "r") as f:
            for linea in f:
                libro = json.loads(linea)
                if libro["codigo"] == codigo_libro:
                    print(f"Se ha devuelto el libro {libro['titulo']}")
                    return True
            else:
                print("El libro no existe.")
                return False


    def agregar_libro(self):
        f = open("libros.txt", "r")
        libros = []
        titulo = input("Titulo del libro: ")
        autor = input("Autor del libro: ")
        ano = input("Año del libro: ")
        editorial = input("Editorial del libro: ")
        codigo = input("Código del libro: ")

        # Abrimos el archivo en modo lectura para leer el contenido del archivo.
        with open("libros.txt", "r") as f:
            for linea in f:
                libro = json.loads(linea)
                libros.append(libro)

        for libro in libros:
            if libro["codigo"] == codigo:
                print(f"El código de libro {codigo} ya existe.")
                return

        # Creamos un nuevo libro con los datos proporcionados por el usuario.
        nuevo_libro = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "editorial": editorial,
            "codigo": codigo
        }

        # Agregamos el nuevo libro a la lista `libros`.
        libros.append(nuevo_libro)

        # Abrimos el archivo en modo escritura para escribir el contenido de la lista `libros`.
        with open("libros.txt", "w") as f:
            for libro in libros:
                f.write(json.dumps(libro))
                f.write("\n")

        f.close()

if __name__ == "__main__":
    l = Libro()

    l.agregar_libro()