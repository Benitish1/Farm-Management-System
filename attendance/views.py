from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import FarmerForm
from .models import Attendance, Farmer

def add_farmer(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farmer_list')
    else:
        form = FarmerForm()
    return render(request, 'attendance/add_farmer.html', { 'form': form })


def farmer_list(request):
    farmers = Farmer.objects.all()
    return render(request, 'attendance/farmer_list.html', {'farmers': farmers})

def mark_attendance(request):
    farmers = Farmer.objects.all()
    date = timezone.now().date()

    if request.method == 'POST':
        for farmer in farmers:
            is_present = f'farmer_{farmer.id}' in request.POST
            Attendance.objects.update_or_create(
                farmer=farmer,
                date=date,
                defaults={'is_present': is_present}
            )
        return redirect('attendance_list')

    return render(request, 'attendance/mark_attendance.html', {'farmers': farmers, 'date': date})

def attendance_list(request):
    records = Attendance.objects.select_related('farmer').order_by('-date')
    return render(request, 'attendance/attendance_list.html', {'records': records})

def farmer_list_json(request):
    farmers = Farmer.objects.all().values('id','name','farm','gender','contract')
    return JsonResponse(list(farmers),safe=False)




