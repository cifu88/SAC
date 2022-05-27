from ProcesoContratacion import ProcesoContratacion

class Notificacion:
    Mensaje:str
    Fecha:str
    Hora: str
    Receptor:str
    ProcesoContratacion : ProcesoContratacion

    def __init__(self, procesoContratacion):
        self.procesoContratacion = ProcesoContratacion 

    def ObtenerMensaje(mensaje):
        return mensaje

    def ObtenerFecha(fecha):
        return fecha

    def ObtenerHora(hora):
        return hora

    def ObtenerReceptor(receptor):
        return receptor