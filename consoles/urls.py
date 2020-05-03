from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000/consoles/   <---- Path so far
    path('', views.index, name="consoles-index"),
    path('<int:id>', views.get_console_by_id, name="console_details"),

]
