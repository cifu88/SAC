from Usuario import Usuario


class RepresentanteLegal(Usuario):
    NombreEntidad : str
    
    def __init__(self, Cargo):
        super().__init__("Representante legal")