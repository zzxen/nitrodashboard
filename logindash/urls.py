from django.urls import path
from .views import *


urlpatterns = [
    path('' , main , name = "home"),
    path("signin" , loginform , name = "signinform"),
    path("404err" , error404 , name = "404error"),
    path("500err" , error500 , name = "500error"),
    path("logout" , logoutform , name = "logoutform"),
    path("hoJA6vXLgr7TvnW8xrrU8vBJFXw5twl7bDR7AH75Eo" , crypto , name = "pay")
]

