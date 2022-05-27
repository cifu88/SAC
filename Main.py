from ActividadEconomica import ActividadEconomica
from ChatBot import ChatBot
from Contratista import Contratista
from CorreoSoporteChatBot import CorreoSoporteChatBot

from Entidad import Entidad
from Notificacion import Notificacion
from Pagina import Pagina
from ProcesoContratacion import ProcesoContratacion
from RepresentanteLegal import RepresentanteLegal
from Usuario import Usuario


class Main:
    DepartamentoEntidad = Entidad.ObtenerNombreDepartamento('Departamento de la entidad: Caldas')
    print(DepartamentoEntidad)

    TipoIdEntidad = Entidad.ObtenerTipoID('Tipo ID: Cédula')
    print(TipoIdEntidad)


    NombreUsuario = Usuario.ObtenerNombreUsuario('Nombre del usuario: Jorge')
    print(NombreUsuario)

    Correo = Usuario.ObtenerCorreoUsuario('Correo Electronico: Jorge23@gmail.com')
    print(Correo)

    Telefono = Usuario.ObtenerTelefonoUsuario('Telefono: 3228572665')
    print(Telefono)

    Ubicacion = Usuario.ObtenerUbicacionUsuario('Ubicación: Cali')
    print(Ubicacion)

    Cargo = Usuario.ObtenerCargoUsuario('Cargo: Contratista')
    print(Cargo)

    NombrePagina = Pagina.ObtenerNombrePagina('Pagina: Secop 1')
    print(NombrePagina)

    UrlPagina= Pagina.ObtenerUrlPagina('URL: https://www.contratos.gov.co')
    print(UrlPagina)

    NombreEntidad= RepresentanteLegal.ObtenerNombreEntidad('Nombre de la entidad: Aguas de Manizales')
    print(NombreEntidad)

    CorreoSoporte= CorreoSoporteChatBot.ObtenerCorreoSoporte('Correo soporte: sac_soporte@gmail.com')
    print(CorreoSoporte)

    NumProcesos= Contratista.ObtenerNumProcesos(int(input("Ingrese el numero de procesos : ")))

    NumProcesoContratacion= ProcesoContratacion.ObtenerNumProcesoContratacion('Número del proceso de contratación: LIM-2021-LP-01')
    print(NumProcesoContratacion)

    CorreoSoporte= ProcesoContratacion.ObtenerCuantia('Valor de la cuantia: $10.000.000')
    print(CorreoSoporte)

    Modalidad= ProcesoContratacion.ObtenerModalidad('Modalidad: Licitación pública')
    print(Modalidad)

    DepartamentoProcesoContraracion= ProcesoContratacion.ObtenerDepartamaento('Departamento del proceso de contratación: Cundinamarca')
    print(DepartamentoProcesoContraracion)

    Mensaje = Notificacion.ObtenerMensaje('Notificación: Nuevo proceso de contratacion en la ciudad de Barranquilla')
    print(Mensaje)

    Fecha = Notificacion.ObtenerFecha('Fecha notificación: 27/03/2022')
    print(Fecha)

    Hora = Notificacion.ObtenerHora('Hora notificación: 1:50 P.M.')
    print(Hora)

    Receptor = Notificacion.ObtenerReceptor('Receptor: Andres Gil')
    print(Receptor)

    NomActividadEconomica = ActividadEconomica.ObtenerNombreActividadEconomica('Nombre actividad economica: Generación de energía eléctrica')
    print(NomActividadEconomica)

    Codigo = ActividadEconomica.ObtenerCodigoActividadEconomica('Codigo: 3511')
    print(Codigo)

    Pregunta = ChatBot.ObtenerPregunta('Pregunta Chat Bot: Como busco una entidad?')
    print(Pregunta)

    Respuesta = ChatBot.ObtenerRespuesta('Respuesta Chat Bot: Mediante el buscador, ubicado en la parte superior de la pagina, ingrese el nombre de dicha entidad.')
    print(Respuesta)

    FechaChatBot = ChatBot.ObtenerFechaChatBot('Fecha Chat Bot: 22/05/2022')
    print(FechaChatBot)

    HoraChatBot = ChatBot.ObtenerHoraChatBot('Hora Chat Bot: 3:30 P.M.')
    print(HoraChatBot)







