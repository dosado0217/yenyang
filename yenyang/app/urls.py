
from django.urls import path
from . import views

app_name = "app"

urlpatterns = [

    # Main Yenyang Customer Showcase
    path("", views.dashboard, name="dashboard"),

]
