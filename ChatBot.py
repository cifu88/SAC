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
        self.correoSoporteChatBot = CorreoSoporteChatBot
        self.entidad = Entidad
        self.usuario = Usuario