class Paciente():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        return print("Nombre completo: {}, edad: {} años.".format(self.nombre,self.edad))

class No_infectado(Paciente):
    def __init__(self, nombre, edad, telefono):
        self.telefono = telefono
        Paciente.__init__(self, nombre, edad)

    def datos(self):
        return print("Nombre completo: {}, edad: {} años, número de teléfono: {}".format(self.nombre,self.edad,self.telefono))

    def string(self):
        return "No_infectado," + self.nombre + "," + str(self.edad) + "," + str(self.telefono) + "," + "X,X,X,X"

class Posible_infectado(Paciente):
    def __init__(self, nombre, edad, direccion, ciudad, estado):
        self.direccion = direccion
        self.ciudad = ciudad
        self.estado = estado
        Paciente.__init__(self, nombre, edad,)

    def datos(self):
        return print("Nombre completo: {}, edad: {} años, direccion: {}, ciudad: {}, estado: {}".format(self.nombre,self.edad,self.direccion,self.ciudad,self.estado))

    def string(self):
        return "Posible_infectado," + self.nombre + "," + str(self.edad) + "," + "X," + self.direccion + "," + self.ciudad + "," + self.estado + "," + "X"

class Infectado(Posible_infectado):
    def __init__(self, nombre, edad, direccion, ciudad, estado, medico):
        self.medico = medico
        Posible_infectado.__init__(self, nombre, edad, direccion, ciudad, estado,)

    def datos(self):
        return print("Nombre completo: {}, edad: {} años, direccion: {}, ciudad: {}, estado: {}, medicado por: {}".format(self.nombre,self.edad,self.direccion,self.ciudad,self.estado,self.medico))

    def string(self):
        return "Infectado," + self.nombre + "," + str(self.edad) + "," + "X," + self.direccion + "," + self.ciudad + "," + self.estado + "," + self.medico