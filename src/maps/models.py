from django.db import models  
from mapbox_location_field.models import LocationField  
  

# Create your models here.

class Location(models.Model):  
 location = LocationField(map_attrs={"center": [74.6370662278128, 42.87254474538025], "marker_color": "blue",'zoom':10})  
