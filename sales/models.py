from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Staff(User):
    POSITIONS = (
        ('J', 'Junior'),
        ('S', 'Senior'),
        ('M', 'Manager'),
    )
    name = models.CharField('Name of staff member', max_length=500)
    position = models.CharField(
        'Position of staff member',
        max_length=1, choices=POSITIONS, default='J'
    )
    commission_percentage = models.DecimalField(
        'Comission percentage', max_digits=5, decimal_places=2
    )

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField('Name of Drink', max_length=500)
    price_per_cup = models.DecimalField(
        'Price per cup', max_digits=5, decimal_places=2
    )
    sold_by = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
