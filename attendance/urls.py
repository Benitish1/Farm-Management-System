
from django.urls import path
from  attendance.views import farmer_list, add_farmer

urlpatterns = [
    path('farmers/', farmer_list, name='farmer_list'),
    path('farmers/add/',add_farmer , name='add_farmer'),
]