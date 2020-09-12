import datetime
from django import forms
from .models import Task

# from django.contrib.admin import widgets

# from django.forms.widgets import SelectDateWidget

class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    due_to = forms.DateField(widget=DateInput)

    #test = forms.DateTimeInput(attrs={'type': 'date'})
    # date = forms.DateField(label='date', widget=widgets.AdminDateWidget())

    def save(self):
        data = self.cleaned_data    
        task_model = Task(title=data['title'],  description=data['description'], due_to=data['due_to'], state='todo',
                          created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
        task_model.save()
        return task_model
        
