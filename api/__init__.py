from flask_restful import Api
from app import flaskAppInstance
from .TaskAPIDelete import Task
from .TaskByIDAPI import TaskByID
from .TaskAPIRead import TaskRead
from .TaskAPIUpdate import TaskUpdate


restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(TaskByID,"/api/v1.0/task/create/<string:nombre>&<string:apellido>&<string:email>&<string:fechaNac>")
restServerInstance.add_resource(Task,"/api/v1.0/task/delete/<string:id>")
restServerInstance.add_resource(TaskRead,"/api/v1.0/task/read/<string:id>")
restServerInstance.add_resource(TaskUpdate,"/api/v1.0/task/update/<string:id>&<string:nombre>&<string:apellido>&<string:email>&<string:fechaNac>")