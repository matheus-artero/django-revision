from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    def clean_description(self):
        data = self.cleaned_data['description']

        if len(data) == 0:
            raise ValidationError('Task shoud have a description')
        
        if len(data) > 150:
            raise ValidationError('Description should be smaller than 150 characters')
        
        return data


    class Meta:
        model = Task
        fields = ('description', 'status')
        labels = {
            'description': 'Describe your task (150 chars limit):',
            'status': 'What is the tasks status currently:'
        }
