from inspect import _void
from ActividadEconomica import ActividadEconomica

class Usuario:
    Id: int
    CorreoElectronico:str
    Nombre : str
    Telefono: int
    Ubicacion : str
    ActividadEconomica : ActividadEconomica
    Cargo = str

    def __init__(self, ActividadEconomica, Id, Nombre):
        self.actividadEconomica = ActividadEconomica
        self.nombre = Nombre
        self.id = Id
    
    def __init__(self, Cargo):
        self.cargo = Cargo

    def ObtenerNombreUsuario(usuario):
        return usuario

    def ObtenerCorreoUsuario(correoElectronico):
        return correoElectronico

    def ObtenerTelefonoUsuario(telefono):
        return telefono
    
    def ObtenerUbicacionUsuario(ubicacion):
        return ubicacion

    def ObtenerCargoUsuario(cargo):
        return cargo