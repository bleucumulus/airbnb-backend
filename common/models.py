from django.db import models

# Create your models here.
class CommonModel(models.Model):
    
    # Common Model Definition
    
     # created_at는 해당 room이 만들어진 시점
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at는 해당 room이 저장되는 시점
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        