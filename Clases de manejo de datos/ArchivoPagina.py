class ArchivoPagina:
    Nombre: str
    URL: str

    def main():
        NumeroPaginas = int(input("Ingrese el número de paginas: "))

        for i in range(NumeroPaginas):
            outfile = open('ArchivoPaginas.txt','a')
            Nombre = input("Ingrese el nombre de la pagina: ")
            URL= input("Ingrese la URL de la pagina: ")
            outfile.write("Nombre de la pagina: " + Nombre + "\n")
            outfile.write("URL: " + URL + "\n\n")
            outfile.write("=======================================================\n")

    main()    