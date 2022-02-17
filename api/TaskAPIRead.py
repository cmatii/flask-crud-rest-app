from api.TaskByIDAPI import Registro
from flask_restful import Resource
from .TaskByIDAPI import TaskByID, getRegistro
import logging as logger

from api import TaskByIDAPI

class TaskRead(Resource):

  
    def get(self,id):

        logger.debug("Inisde the read method Size of registro {}, checking for id: {}".format(len(TaskByIDAPI.getRegistro()), id)) 
        return getUser(id)

   

def getUser(id):
    Registro=getRegistro()
    if(len(Registro) > 0):
        for user in Registro:
            logger.debug(user.nombre)
            if(str(user.id) == id):
                logger.debug("Usuario encontrado ")
                #return user
                return {"message" : " Nombre: {}, Apellido: {} , Email: {}, FechaNacimiento: {}".format(user.nombre, user.apellido, user.email, user.fechaNac)},200

            else:
                return {"message" : "400 BAD REQUEST"},400
    else:
        return {"message" : "400 BAD REQUEST, THERE IS NO USER TO SHOW"},400
    logger.debug("Usuario NO encontrado ")

            
        
        