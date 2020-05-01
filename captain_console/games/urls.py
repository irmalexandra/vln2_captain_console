from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000/main
    path('', views.index, name="main-index"),

]