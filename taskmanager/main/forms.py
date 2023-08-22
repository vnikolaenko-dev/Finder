from .models import *
from django.forms import ModelForm, TextInput, Textarea, FileField


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',
                'maxLength': '20'
            }),

            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'image']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя',
                'maxLength': '20'
            }),

            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email'
            }),

            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            })
        }


class UserFormOpen(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': TextInput(attrs={
                'class': 'myfield',
                'placeholder': 'Введите email'
            }),

            'password': TextInput(attrs={
                'class': 'myfield',
                'placeholder': 'Введите пароль'
            })
        }
        required_css_class = "field"
        error_css_class = "error"


class TextForm(ModelForm):
    class Meta:
        model = Text
        fields = ['text', 'email', 'sent']
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите что-нибудь...'
            })
        }


