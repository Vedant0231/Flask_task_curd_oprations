"""program to get access to todo list"""

from flask import Flask
from views import Todolist, Todo 
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
     
"""url or we can say end points"""
api.add_resource(Todolist, '/todo')
api.add_resource(Todo, "/todo/<int:todo_id>")
