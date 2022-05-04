from CorreoSoporteChatBot import CorreoSoporteChatBot
from Entidad import Entidad

class ChatBot:
    Pregunta: str
    Respuesta: Entidad 
    Fecha: str
    Hora: str
    CorreoSoporteChatBot: CorreoSoporteChatBot 


    def main():
        NumeroPreguntas = int(input("Ingrese el numero de preguntas : "))

        for i in range(NumeroPreguntas):
            outfile = open('ChatBot.txt','a')
            Pregunta = input("Ingrese la pregunta: ")
            Respuesta= input("Ingrese la respuesta: ")
            outfile.write("Pregunta: " + Pregunta + "\n")
            outfile.write("Respuesta: " + Respuesta + "\n\n")

    main()    