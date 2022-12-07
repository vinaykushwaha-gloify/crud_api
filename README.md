# crud_api
crud_api with signup and login

using simple jwt authentication

Admin user :- python123@gmail.com Admin password :- 2211

At first clone this project- Install this module :- pip install virtualenv Then create virtual env. in which directory your project is cloned usig this command :- virtualenv venv Then activate your virtual env after your dir :- .\venv\Scripts\activate. Then go to project folder and run this command :- pip install -r requirements.txt.

Then run this command to run the project :- python manage.py runserver

Then....

POST http://127.0.0.1:8000/api/signup/ responsible for signup with name,email,mobile and password with post method. 
POST http://127.0.0.1:8000/api/login/ responsible for signin with email and password and return a valid token with post method. 
GET http://127.0.0.1:8000/api/get/user/  get all user whaterever users created.
POST http://127.0.0.1:8000/api/task/create/ responsible for create task data with post method with a valid token because this is protected endpoint. 
task_field is - task_name,priority and description.
GET http://127.0.0.1:8000/api/show/task/ responsible for get the all available task with get method with a valid token because this is protected endpoint. 
GET http://127.0.0.1:8000/api/task/update/1 responsible for retrieve single data by id for valid authentication token. 
PUT http://127.0.0.1:8000/api/task/update/1 responsible for update single task-data by id for valid authentication token. 
DELETE http://127.0.0.1:8000/api/task/update/1 responsible for delete single task-data by id for valid authentication token.

Thanks................

