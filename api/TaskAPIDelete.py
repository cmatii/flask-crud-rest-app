from api.TaskByIDAPI import Registro
from flask_restful import Resource
from .TaskByIDAPI import TaskByID, getRegistro, setRegistro
import logging as logger

from api import TaskByIDAPI

class Task(Resource):

  
    def delete(sef, id):
        logger.debug("Inisde the delete method Size of registro {}, id: {}".format(len(TaskByIDAPI.getRegistro()), id))
        delete(id)
        return {"message" : "User deleted"},200
   

def delete(id):
    Registro=getRegistro()
    c=len(Registro)
    if(c > 0):
        for i in range(0,len(Registro)):
            aux=Registro[i]
            if(str(aux.id) == id):
                Registro.pop(i)
                logger.debug("User {} Removed, previous index= {}, actual index={}".format( id,c,len(Registro)))
                setRegistro(Registro)
                return {"message" : "User deleted"},200
            else:
                return {"message" : "400 BAD REQUEST, NO MATCH ID"},400
    else:
          return {"message" : "400 BAD REQUEST, THERE IS NO USER TO DELETE"},400
    logger.debug("Nothing Deleted {}".format(type(aux.id)))
            
        
        