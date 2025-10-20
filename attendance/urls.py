
from django.urls import path
from  attendance.views import farmer_list, add_farmer

urlpatterns = [
    # path('farmers/', farmer_list, name='farmers'),
    path('farmers/add/',add_farmer , name='farmer_create'),
]