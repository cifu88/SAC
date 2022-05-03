from ProcesoContratacion import ProcesoContratacion

class Notificacion:
    Mensaje:str
    Fecha:str
    Hora: str
    Receptor:str
    ProcesoContratacion : ProcesoContratacion

    def __init__(self, procesoContratacion):
        self.procesoContratacion = ProcesoContratacion 