from ActividadEconomica import ActividadEconomica

class Usuario:
    Id: int
    CorreoElectronico:str
    Nombre : str
    Telefono: int
    Ubicacion : str
    ActividadEconomica : ActividadEconomica

    def __init__(self, actividadEconomica, Id, Nombre):
        self.actividadEconomica = ActividadEconomica
        self.nombre = Nombre
        self.id = Id

    def main():
        NumeroUsuarios = int(input("Ingrese el número de usuarios: "))

        for i in range(NumeroUsuarios):
            outfile = open('Usuarios.txt','a')
            Id = input("Ingrese el ID: ")
            CorreoElectronico= input("Ingrese el correo electronico: ")
            Nombre= input("Ingrese el nombre completo: ")
            Telefono= input("Ingrese el numero de telefono: ")
            Ubicacion= input("Ingrese la ubicacion: ")
            ActividadEconomica= input("Ingrese la actividad economica: ")
            outfile.write("ID: " + Id + "\n")
            outfile.write("Correo Electronico: " + CorreoElectronico + "\n\n")
            outfile.write("Nombre: " + Nombre + "\n\n")
            outfile.write("Telefono: " + Telefono + "\n\n")
            outfile.write("Ubicacion: " + Ubicacion + "\n\n")
            outfile.write("Actividad economica: " + ActividadEconomica + "\n\n")
            outfile.write("=======================================================\n")


    main()