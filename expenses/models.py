from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = [
    ("Food", "Food"),
    ("Rent", "Rent"),
    ("Utilities", "Utilities"),
    ("Transport", "Transport"),
    ("Entertainment", "Entertainment"),
    ("Other", "Other"),
]


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.amount})"
