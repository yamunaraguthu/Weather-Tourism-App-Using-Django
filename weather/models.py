from django.db import models

class CityImage(models.Model):
    city_name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='city_images/')

    def __str__(self):
        return self.city_name

class CountryImage(models.Model):
    country_code = models.CharField(max_length=2, unique=True)  # e.g., "IN" for India
    image = models.ImageField(upload_to='country_images/')

    def __str__(self):
        return self.country_code