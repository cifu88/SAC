from inspect import _void
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

    

