from ProcesoContratacion import ProcesoContratacion
from Usuario import Usuario

class Contratista(Usuario):

    ProcesoContratacion : ProcesoContratacion
    NumProcesos: str

    def __init__(self,procesoContratacion):
        self.procesoContratacion = ProcesoContratacion