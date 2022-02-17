from pickle import FALSE, TRUE
from flask_restful import Resource
import logging as logger
import re
import uuid
from datetime import datetime

class TaskByID(Resource):

    def post(self,nombre,apellido,email,fechaNac):
        logger.debug("Inside the post method of Create")
        try:
            emailExist(email)
            check(email)
            valiDate(fechaNac )

            creation(nombre,apellido,email,fechaNac)
            logger.debug(len(Registro))
            return {"message" : "Id: {}, Nombre: {}, apellido: {}, Email: {}, FechaNacimiento: {}".format(Registro[len(Registro)-1].id,Registro[len(Registro)-1].nombre, Registro[len(Registro)-1].apellido, Registro[len(Registro)-1].email, Registro[len(Registro)-1].fechaNac)},200
        except:
            return {"message": "400 BAD REQUEST, THERE IS AN ERROR ON THE USER TO BE ADDED"},400




def emailExist(email):
    for user in Registro:
        if(user.email == email):
            raise Exception("Sorry, no duplicated emails accepted")


def check(email):

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")
        raise Exception("Sorry, bad emails structure not accepted")

def valiDate(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

     

def creation(nombre,apellido,email,fechaNac):
    usuario = Usuario(nombre, apellido, email, fechaNac)
    Registro.append(usuario)
    

class Usuario():
    def __init__(self,nombre, apellido,email,fechaNac):
        self.id = uuid.uuid4()
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.fechaNac = fechaNac



Registro = list()


def getRegistro():
    return Registro

def setRegistro(Registro):
    Registro=Registro