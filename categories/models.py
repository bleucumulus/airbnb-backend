from django.db import models
from common.models import CommonModel

# Create your models here.
class Category(CommonModel):
    
    class CategoryKindChoices(models.TextChoices):
        
        # Room category
        ROOMS = "rooms", "Rooms"
        # Experiences category
        EXPERIENCES = "experiences", "Experiences"
       
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=20, choices=CategoryKindChoices.choices)
    
    def __str__(self) -> str:
        return f"{self.kind.title()}: {self.name}"
    
    
    class Meta:
        verbose_name_plural="Categories"