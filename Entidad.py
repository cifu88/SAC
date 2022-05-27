
from ProcesoContratacion import ProcesoContratacion
from Usuario import Usuario
class Entidad:
    Id: int
    TipoId: str
    ProcesoContratacion: ProcesoContratacion
    Usuario: Usuario
    Departamento: str

    def ObtenerNombreDepartamento(departamento):
        return departamento

    def ObtenerTipoID(tipoId):
        return tipoId
