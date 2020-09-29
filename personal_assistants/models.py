import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.utils.timezone import now
from django.core.exceptions import ValidationError

class Task(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(1)]) 
    description = models.TextField()
    state = models.CharField(max_length=4)
    due_to = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Tasks'

