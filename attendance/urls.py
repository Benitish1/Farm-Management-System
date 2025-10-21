
from django.urls import path
from  attendance.views import farmer_list, add_farmer, mark_attendance, attendance_list, farmer_list_json

urlpatterns = [
    path('farmers/', farmer_list, name='farmer_list'),
    path('farmers/add/',add_farmer , name='add_farmer'),
    path('farmers/attendance/',mark_attendance , name='mark_attendance'),
    path('farmers/attendance/list/', attendance_list, name='attendance_list'),
    path('farmers/json/', farmer_list_json, name='farmer_list_json'),
]