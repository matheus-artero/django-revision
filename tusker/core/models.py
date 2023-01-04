from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ("O", "open"),
    ("P", "in progress"),
    ("C", "closed")
)

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='O')

    def __str__(self):
        return f"{self.description} owned by {self.user} is {self.get_status_display()}"