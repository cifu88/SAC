from CorreoSoporteChatBot import CorreoSoporteChatBot
from Entidad import Entidad
class ChatBot:
    Pregunta: str
    Respuesta: Entidad 
    Fecha: str
    Hora: str
    CorreoSoporteChatBot: CorreoSoporteChatBot 

    def __init__(self, correoSoporteChatBot, entidad):
        self.correoSoporteChatBot = CorreoSoporteChatBot
        self.entidad = Entidad