

# Create your models here.
from django.db.models import CheckConstraint, Q, constraints
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
CATEGORY_CHOICES = (
    ("1","Electronics"),
    ("2", "Appliances"),
    ("3","Home Decor"),
    ("4","Misc"),
    ("5","Clothing"),
    ("6","Footwear"),
    ("7","Sports"),
    ("8","Health and Beauty"),
)

class Item(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices = CATEGORY_CHOICES, default='4')
    quantity = models.PositiveIntegerField()
    description = models.TextField(max_length=250)
    itemcode = models.PositiveIntegerField(unique=True)

    class Meta:
        db_table = "inventory"
        




        

