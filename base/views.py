from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import News

# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request) 
            messages.success(request, 'Logout Successful')
            return redirect('registration/login.html')
    # Nếu là admin -> vào trang admin
    if request.user.is_staff or request.user.is_superuser:
        return redirect('/admin/')  # Django admin dashboard

    # Nếu là user thường -> vào trang home
    return render(request, "home.html")
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('base:login')
    else:
        form = UserCreationForm()
    return render(request,"registration/signup.html",{"form":form})
def news(request):
   newss = News.objects.all()
   context = {'newss':newss}
   return render(request,'news/news.html', context)

## cap nhat avata
from django.shortcuts import render, redirect
from .forms import AvatarUpdateForm
from .models import UserProfile

def update_avatar(request):
    # Kiểm tra nếu user chưa có UserProfile thì tạo mới
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = AvatarUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/profile/')
    else:
        form = AvatarUpdateForm(instance=profile)

    return render(request, 'update_avatar.html', {'form': form})

from django.shortcuts import render
from .models import UserProfile

def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': user_profile})
## Quan li task

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
def task_list(request):
    """Hiển thị danh sách công việc"""
    tasks = Task.objects.all().order_by('-created')
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    """Thêm công việc mới"""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/task_list/')
    else:
        form = TaskForm()
    return render(request, 'task/task_form.html', {'form': form})

def task_complete(request, task_id):
    """Đánh dấu công việc đã hoàn thành"""
    task = get_object_or_404(Task, id=task_id)
    task.mark_completed()
    return redirect('/task_list/')


