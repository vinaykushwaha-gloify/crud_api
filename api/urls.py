from django.urls import path
from api.views import *
## define here urls

urlpatterns = [
    path("signup/", SignUpUserView.as_view(), name="sign-up-user"),
    path("login/", LoginUserView.as_view(), name="login-user"),
    path("get/user/", GetAllUser.as_view(), name="get-all-user"),
    path("task/create/", TaskCreate.as_view(), name="create-task"),
    path("show/task/", ShowAllTask.as_view(), name="show-all-task"),
    path("task/update/<int:pk>", TaskUpdateDelete.as_view(), name="task-update-delete")

]


