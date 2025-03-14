from django.contrib import admin
from .models import News
from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link', 'completed', 'created')
    readonly_fields = ('created',)  # Trường chỉ đọc

admin.site.register(News, NewsAdmin)

from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created", "finished")  # Hiển thị cột
    list_filter = ("status",)  # Bộ lọc theo trạng thái
    search_fields = ("title",)  # Cho phép tìm kiếm theo tiêu đề
    ordering = ("-created",)  # Sắp xếp theo thời gian tạo mới nhất trước

admin.site.site_header = "Task Management Admin"
admin.site.site_title = "Task Admin"
admin.site.index_title = "Quản lý Công Việc"
