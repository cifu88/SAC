class ActividadEconomica:
    NombreActividadEconomica: str
    CodigoActividadEconomica: int


    def main():
        NumeroActividades = int(input("Ingrese el número de actividades: "))

        for i in range(NumeroActividades):
            outfile = open('Actividad.txt','a')
            NombreActividadEconomica = input("Ingrese el nombre de la actividad económica: ")
            CodigoActividadEconomica= input("Ingrese el código de la actividad económica: ")
            outfile.write("Nombre de la actividad economica: " + NombreActividadEconomica + "\n")
            outfile.write("Codigo: " +CodigoActividadEconomica + "\n\n")


    main()