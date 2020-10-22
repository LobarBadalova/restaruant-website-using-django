from django.contrib import admin

# Register your models here.
from .models import Meals, Category

class MealsAdmin(admin.ModelAdmin):
	list_display=['name', 'preparation_time', 'category']
	search_fields=['title', 'content']

admin.site.register(Meals, MealsAdmin)
admin.site.register(Category)
