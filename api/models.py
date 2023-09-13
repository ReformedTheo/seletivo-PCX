from django.db import models

# Create your models here.

CARGO_CHOICES = [
        ('DE', 'Developer'),
        ('MA', 'Manager'),
        ('AN', 'Analist'),
        ('TE', 'Tester'),
        ('SU', 'Support'),
    ]

class Employee(models.Model):     
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=2, choices=CARGO_CHOICES, default='DE')
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    admission = models.DateField()
    active = models.BooleanField(default=1)

    def __str__(self):
        return self.nome