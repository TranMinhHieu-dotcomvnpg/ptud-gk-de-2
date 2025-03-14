from django.db import models

# Create your models here.
from django.db import models

from django.db import models
from django.utils import timezone

class News(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Công nghệ'),
        ('sports', 'Thể thao'),
        ('business', 'Kinh doanh'),
        ('entertainment', 'Giải trí'),
        ('other', 'Khác'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='news_images/', default='fallback.png', blank=True, null=True)
    link = models.URLField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  # Cập nhật thời gian sửa đổi

    def mark_completed(self):
        """Đánh dấu tin tức đã xử lý"""
        self.completed = True
        self.updated = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"

    def __repr__(self):
        return f"<News(title={self.title}, created={self.created}, completed={self.completed})>"

from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.utils.timezone import now
## phân quyền catalot
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    STATUS_CHOICES = [
        ("pending", "Chưa hoàn thành"),
        ("completed", "Đã hoàn thành"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(null=True, blank=True)  # Lưu thời gian hoàn thành
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 

    def mark_completed(self):
        """Đánh dấu công việc là hoàn thành"""
        self.status = "completed"
        self.finished = now()  # Ghi lại thời gian hoàn thành
        self.save()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='default.png')

    def __str__(self):
        return self.user.username
