from django.contrib import admin
from .models import Course, CarouselImage

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'stars', 'price', 'link']
    list_display = ('title', 'price', 'stars', 'is_trending')
    list_filter = ('is_trending',)

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')  # Assuming CarouselImage has these fields
