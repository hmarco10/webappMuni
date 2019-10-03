from django import forms
from .models import owner, Student, Subject

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'
		
		widgets = {
			'name':forms.TextInput(attrs={'class':'form-control'}),
			'last_name':forms.TextInput(attrs={'class':'form-control'}),
			'subject_student':forms.SelectMultiple(attrs={'class':'form-control'}),
		}