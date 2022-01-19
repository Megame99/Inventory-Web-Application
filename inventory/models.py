
# Create your models here.

from django.db import models

CATEGORY_CHOICES = (
    ("Electronics","Electronics"),
    ("Appliances", "Appliances"),
    ("Home Decor","Home Decor"),
    ("Misc","Misc"),
    ("Clothing","Clothing"),
    ("Footwear","Footwear"),
    ("Sports","Sports"),
    ("Health and Beauty","Health and Beauty"),
)

class Item(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices = CATEGORY_CHOICES, default='6')
    quantity = models.PositiveIntegerField()
    description = models.TextField(max_length=250)
    itemcode = models.PositiveIntegerField(unique=True)

    class Meta:
        db_table = "inventory"
        




        

