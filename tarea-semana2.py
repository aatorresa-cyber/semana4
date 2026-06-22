def _init_(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
def Estudiante(self):
        print(f"{self.nombre} está estudiando {self.carrera}.")
def mostrar_datos(self):
        print("\n----- DATOS DEL ESTUDIANTE -----")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")



estudiante1 = Estudiante("Alicia Torres", 30, "Ingeniería Tecnologías de la Información")
estudiante2 = Estudiante("Dominik Naranjo", 24, "Turismo")


estudiante1.mostrar_datos()
estudiante1.estudiar()

estudiante2.mostrar_datos()
estudiante2.estudiar()