class User():
    def __init__(self, nombre, edad, correo, tipo_usuario, proyecto_curricular, facultad, codigo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.tipo_usuario = tipo_usuario
        self.proyecto_curricular = proyecto_curricular
        self.facultad = facultad
        self.codigo = codigo
    
class Admin(User):
    def __init__(self, nombre, edad, correo, proyecto_curricular, facultad, codigo):
        super().__init__(nombre, edad, correo, proyecto_curricular, facultad, codigo)
        self.tipo_usuario = Admin

class Estudiante(User):
    def __init__(self, nombre, edad, correo, proyecto_curricular, facultad, codigo):
        super().__init__(nombre, edad, correo, proyecto_curricular, facultad, codigo)
        self.tipo_usuario = Estudiante

class Profesor(User):
    def __init__(self, nombre, edad, correo, proyecto_curricular, facultad, codigo):
        super().__init__(nombre, edad, correo, proyecto_curricular, facultad, codigo)
        self.tipo_usuario = Profesor

