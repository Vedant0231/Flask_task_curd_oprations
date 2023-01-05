from database import todolist
from flask_restful import Resource, reqparse

todo_post = reqparse.RequestParser()

todo_post.add_argument('task', type = str, help = "task is required", required = True)
todo_post.add_argument('time_duration', type = str, help = "time duration is required", required = True)

"""api to get todo task by id"""
class Todo(Resource):

    """api to get task by id"""
    def get(self,todo_id):

        return todolist[todo_id]


    """api to post task"""
    def post(self, todo_id):

        args = todo_post.parse_args()    

        """check todo_id is already there or not"""
        if todo_id in todolist:

            return("id already used")

        todolist[todo_id]= {'task':args['task'], 'time_duration':args['time_duration']}  

        return todolist[todo_id]   


    """api to update task"""
    def put(self, todo_id):

        args = todo_post.parse_args()
        todolist[todo_id]= {'task':args['task'], 'time_duration':args['time_duration']} 

        return todolist[todo_id]   


    """api to delete task """
    def delete(self, todo_id):

        del todolist[todo_id]    

        return f"data number {todo_id} has been deleted "


"""api to get whole todolist"""
class Todolist(Resource):

    def get(self):

        return todolist