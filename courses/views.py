from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Course, CarouselImage

def index(request):
    courses = Course.objects.exclude(is_trending=True) 
    carousel_images = CarouselImage.objects.all()
    trending_courses = Course.objects.filter(is_trending=True)
    return render(request, 'index.html', {
        'courses': courses,
        'carousel_images': carousel_images,
        'trending_courses': trending_courses,
    })
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')  # ✅ Admins go to Django Admin Panel
            else:
                return redirect('home')     # ✅ Normal users go to homepage
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('home')
    return redirect('home')  # fallback if request is not POST

def user_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('home')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('home')

        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        user.save()
        messages.success(request, "Registration successful.")
        return redirect('home')

def user_logout(request):
    logout(request)
    return redirect('home')


from django.shortcuts import render
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


from django.shortcuts import get_object_or_404

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'courses/course_detail.html', {'course': course})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import PurchasedCourse  # or whatever model you use

@login_required
def home(request):
    purchased_courses = PurchasedCourse.objects.filter(user=request.user)
    return render(request, 'courses/home.html', {'purchased_courses': purchased_courses})

