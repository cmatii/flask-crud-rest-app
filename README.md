# flask-crud-rest-app

flask-crud-rest-app is a Api Rest Service for test purpose, there has been developed using Python 3.9 and Flask a framework.

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