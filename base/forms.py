from django import forms
from .models import News

from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Nhập tiêu đề tin tức",
            "class": "form-control"
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            "placeholder": "Mô tả chi tiết...",
            "rows": 3,
            "class": "form-control"
        })
    )
    link = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            "placeholder": "Nhập đường link (nếu có)",
            "class": "form-control"
        })
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control-file"
        })
    )
    category = forms.ChoiceField(
        choices=News.CATEGORY_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = News
        fields = ["title", "description", "link", "image", "category"]  # Không cho user chỉnh `completed`


from django import forms
from .models import Task, Category

from django import forms
from django.contrib.auth.models import User
from .models import Task

class TaskForm(forms.ModelForm):
    finished = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'category', 'assigned_to', 'finished']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'assigned_to': forms.Select(attrs={'class': 'form-select'}),  # 🟢 Chọn user được giao nhiệm vụ
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


from django import forms
from .models import UserProfile

from django import forms
from .models import UserProfile

class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']  # Đảm bảo 'avatar' là field tồn tại trong model UserProfile

### user form

