from CorreoSoporteChatBot import CorreoSoporteChatBot
from Entidad import Entidad
from Usuario import Usuario
class ChatBot:
    Usuario : Usuario
    Pregunta: str
    Respuesta: Entidad 
    Fecha: str
    Hora: str
    CorreoSoporteChatBot: CorreoSoporteChatBot 

    def __init__(self, correoSoporteChatBot, entidad, usuario):
        self.CorreoSoporteChatBot = correoSoporteChatBot
        self.entidad = Entidad
        self.usuario = Usuario

    def ObtenerPregunta(pregunta):
        return pregunta
    def ObtenerRespuesta(respuesta):
        return respuesta
    def ObtenerFechaChatBot(fecha):
        return fecha
    def ObtenerHoraChatBot(hora):
        return hora
