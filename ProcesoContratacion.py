from ActividadEconomica import ActividadEconomica
from Pagina import Pagina


class ProcesoContratacion:
    NumeroProceso : str
    Cuantia : int
    Modalidad : str
    ActividadEconomica : ActividadEconomica
    Departamento : str
    Pagina : Pagina

    def __init__(self, actividadEconomica, pagina):
        self.actividadEconomica = ActividadEconomica
        self.pagina = Pagina
        