class Alumno:
    def __init__(self, nombre, apellido, edad, curso):
        self.nombre = nombre.capitalize()
        self.apellido = apellido.capitalize()
        self.edad = edad
        self.curso = curso.capitalize()
        # .capitalize() convierte la primera letra en mayúscula y el resto en minúscula

    def programar(self):
        print(f"El alumno {self.nombre} está programando")


nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = input("Ingresá tu edad: ")
curso = input("Ingresá tu curso: ")

alumno = Alumno(nombre, apellido, edad, curso)

alumno.programar()