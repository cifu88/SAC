from ActividadEconomica import ActividadEconomica

class ArchivoUsuario:
    Id: int
    CorreoElectronico:str
    Nombre : str
    Telefono: int
    Ubicacion : str
    ActividadEconomica : ActividadEconomica
    Cargo = str

    def __init__(self, ActividadEconomica, Id, Nombre):
        self.actividadEconomica = ActividadEconomica
        self.nombre = Nombre
        self.id = Id
    
    def __init__(self, Cargo):
        self.cargo = Cargo

    def main():
        NumeroUsuarios = int(input("Ingrese el número de usuarios: "))

        for i in range(NumeroUsuarios):
            outfile = open('ArchivoUsuarios.txt','a')
            Id = input("Ingrese el ID: ")
            CorreoElectronico= input("Ingrese el correo electronico: ")
            Nombre= input("Ingrese el nombre completo: ")
            Telefono= input("Ingrese el numero de telefono: ")
            Ubicacion= input("Ingrese la ubicacion: ")
            ActividadEconomica= input("Ingrese la actividad economica: ")
            Cargo= input("Ingrese si es Contratista o Representante legal: ")
            outfile.write("ID: " + Id + "\n")
            outfile.write("Correo Electronico: " + CorreoElectronico + "\n\n")
            outfile.write("Nombre: " + Nombre + "\n\n")
            outfile.write("Telefono: " + Telefono + "\n\n")
            outfile.write("Ubicacion: " + Ubicacion + "\n\n")
            outfile.write("Actividad economica: " + ActividadEconomica + "\n\n")
            outfile.write("Cargo : " + Cargo + "\n\n")
            outfile.write("=======================================================\n")


    main()