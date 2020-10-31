import datetime
from django import forms
from .models import Task, Category


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    due_to = forms.DateField(widget=DateInput)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

    def save(self):
        data = self.cleaned_data
        task_model = Task(
            title=data['title'],  
            description=data['description'], 
            due_to=data['due_to'], 
            state='todo',
            created_at=datetime.datetime.now(), 
            updated_at=datetime.datetime.now(),
            category = data['category']
            )
        task_model.save()
        return task_model
      


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name'].capitalize()
        if Category.objects.filter(name=name).exists():
            raise forms.ValidationError("This category already exists %(name)s", params={'name': name})
        return name


    # def save(self):
    #     data = self.cleaned_data
    #     categories = Category(name=data['name'])
    #     categories.save()
    #     return categories