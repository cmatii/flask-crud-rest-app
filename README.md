# flask-crud-rest-app

flask-crud-rest-app is a Api Rest Service for test purpose, there has been developed using Python 3.9 and Flask as framework.

The testing is suggested to be performed using postman app, with the formula listed forward in this README.

This project was created using Anaconda as package manager, so it is highly recommended use it on testing this app.

## Git clone the application

## Create a virtual environment inside the application 

```python
    virtualenv -p /usr/bin/python3.4 venv    

    source venv/bin/activate
```
If your using Anaconda : 
```python
	conda create -n "myenv" python=3.9.x

	conda activate myenv
```

## Install Python modules

```python

   pip3.4 install -r requirements.txt 
    
```
If your using Anaconda: 
```python
	conda install --file requirements.txt
```
## Run the application using

```python

    python app.py

```

## Testing on POSTMAN

There has been added a config file calle Test *

> Flsk.postman_collection.json

* It can be imported into a Postman app, to make the testing process easier.
* Look for it on the Test folder.

## End Points
  

| EndPoint | Input  | Output |
|--|--|--|
| http://192.168.1.170:5000/api/v1.0/task/create/ | {Nombre}&{Apellido}&{Email}&{fechaNacimiento} | It's everything goes fine should receive, the same information of the user added, otherwise should have a 400 BAD REQUEST |
| http://192.168.1.170:5000/api/v1.0/task/delete/ | {id} |Should get a message indicating that the user of the id delivered there has been deleted, otherwise should throw an 400 Bad Request Error  |
| http://192.168.1.170:5000/api/v1.0/task/read/| {id} | Should return the values of the user related with the parsed id, otherwise should throw and 400 Bad Request Error  |
| http://192.168.1.170:5000/api/v1.0/task/update/ | {id}&{Nombre}&{Apellido}&{Email}&{fechaNacimiento} | if everythig goes fine should recive a message indicating that the user has been added to the related id, otherwise should thorw and 400 Bad Request |