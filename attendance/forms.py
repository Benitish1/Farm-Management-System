from django import forms
from .models import Farmer, Attendance

#Form for Farmer model

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name','farm']
       
       #to get all fields at the same time without specifying them
       # fields='__all__' 

        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter farmer name'
        }),
         'farm':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter farm name'
        }),
        }

        # #form for Attendance model
        # class AttendanceForm(form.ModelForm):