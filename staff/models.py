# Create your models here.
from django.db import models

class StaffData(models.Model):
    id = models.IntegerField(primary_key=True)
    name_full = models.TextField(blank=True,null=True)  # Full name of staff
    name_native = models.TextField( blank=True,null=True)  # Native name (optional)
    name_alternative = models.TextField( blank=True,null=True)  # Alternative name (optional)
    language = models.TextField( blank=True,null=True)  # Language spoken by the staff
    description = models.TextField(blank=True,null=True)  # Description (optional)
    image = models.URLField(blank=True, null=True)
      # Image (optional)
    site_url = models.URLField(blank=True,null=True, )  # Website URL (optional)
    staff_media=models.TextField(blank=True, null=True) # Staff media (optional)
    occupation = models.TextField( blank=True,null=True)  # Occupation (optional)

    def __str__(self):
        return self.name_full  # To display the staff name when accessing the model

