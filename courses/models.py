from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='course_images/')
    stars = models.IntegerField(default=4)  # Numeric star rating
    price = models.DecimalField(max_digits=6, decimal_places=2)
    link = models.URLField(blank=True)  # Optional link
    category = models.CharField(max_length=100, default='General')  # optional
    is_trending = models.BooleanField(default=True)  # For special filtering

    def __str__(self):
        return self.title

class CarouselImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='carousel_images/')

    def __str__(self):
        return self.title
    
slug = models.SlugField(unique=True)


class PurchasedCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"


