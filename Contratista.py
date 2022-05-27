from ProcesoContratacion import ProcesoContratacion
from Usuario import Usuario

class Contratista(Usuario):

    ProcesoContratacion : ProcesoContratacion
    NumProcesos: str

    def __init__(self, procesoContratacion):
        self.procesoContratacion = ProcesoContratacion
    
    def __init__(self, Cargo):
        super().__init__("Contratista")

    def ObtenerNumProcesos(numProcesos):
        return numProcesos
