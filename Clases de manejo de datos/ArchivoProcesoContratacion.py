from ActividadEconomica import ActividadEconomica
from Pagina import Pagina


class ArchivoProcesoContratacion:
    NumeroProceso : str
    Cuantia : int
    Modalidad : str
    ActividadEconomica : ActividadEconomica
    Departamento : str
    Pagina : Pagina

    def __init__(self, actividadEconomica, pagina):
        self.actividadEconomica = ActividadEconomica
        self.pagina = Pagina

    def main():
        NumeroProcesos = int(input("Ingrese la cantidad de procesos de contratación: "))

        for i in range(NumeroProcesos):
            outfile = open('ArchivoProcesosContratacion.txt','a')
            NumeroProceso = input("Ingrese el número del proceso: ")
            Cuantia= input("Ingrese la cuantia del proceso: ")
            Modalidad = input("Ingrese la modalidad del proceso: ")
            ActividadEconomica = input("ingrese la actividad económica del proceso :")
            Departamento = input("ingrese el departamento de ejecución del proceso: ")
            Pagina = input("Ingrese la página del proceso: ")
            outfile.write("Número del proceso: " + NumeroProceso + "\n")
            outfile.write("Cuantia del proceso: " + Cuantia + "\n")
            outfile.write("Modalidad del proceso: " + Modalidad + "\n")
            outfile.write("Actividad economica del proceso: " + ActividadEconomica + "\n")
            outfile.write("Departamento del proceso: " + Departamento + "\n")
            outfile.write("Pagina del proceso: " + Pagina + "\n\n")
            outfile.write("=======================================================\n")

    main()  