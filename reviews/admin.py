from django.contrib import admin
from .models import Review

class WordFilter(admin.SimpleListFilter):
    
    title = "Filter by Words !"
    
    # parameter_name (일단 임시로)
    parameter_name = "parameterName"

    def lookups(self, request, model_admin):
        return [
            # 여기에 다 써도 괜찮은 건진 모르겠는데 단어를 필터링하는 필터를 어떻게 또 만들 수 있는 지에 대해선 아직 안해봄
            ("good","Good",),
            ("bad","Bad",),
        ]
        
    def queryset(self, request, reviews):
        word = self.value()
        if word == "good":
            #return reviews.filter(payload__contains=word)
            return reviews.filter(rating__gte=3)
        elif word == "bad":
            return reviews.filter(rating__lt=3)
        else:
            return reviews
        
# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__", "payload",
    )
    
    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
    )