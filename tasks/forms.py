from django.forms import ModelForm, TextInput, Textarea, DateInput
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'rows': '3'
            }),
            'due_date': DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }
