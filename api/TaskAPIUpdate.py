from api.TaskByIDAPI import Registro
from flask_restful import Resource
from .TaskByIDAPI import TaskByID, getRegistro, setRegistro, emailExist, check, valiDate
import logging as logger
from api import TaskByIDAPI

class TaskUpdate(Resource):

  
    def put(self,id,nombre,apellido,email,fechaNac):

        logger.debug("Inisde the PUT method Size of registro {}, checking for id: {}".format(len(TaskByIDAPI.getRegistro()), id))
        return update(id, nombre,apellido,email,fechaNac)

   

def update(id,nombre,apellido,email,fechaNac):
    Registro=getRegistro()
    c=len(Registro)
    for i in range(0,len(Registro)):
        user=Registro[i]
        if(str(user.id) == id):
            logger.debug("User {} Exist".format(id))
            emailExist(email)
            check(email)
            valiDate(fechaNac)
            user.nombre=nombre
            user.apellido=apellido
            user.email=email
            user.fechaNac=fechaNac
            Registro[i]=user
            setRegistro(Registro)
            #return {"message" : "User updated"},200
            return {"message" : "Usuario Encontrado: Nombre: {}, Apellido: {} , Email: {}, FechaNacimiento: {}".format(user.nombre, user.apellido, user.email, user.fechaNac)},200
        else:
            logger.debug("Nothing Updated {}".format(type(user.id)))
            return {"message": "400 BAD REQUEST, THERE IS NO USER TO UPDATE"},400