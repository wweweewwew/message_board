from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['text']
        labels = {'text': 'Текст объявления'}
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Введите текст объявления...'}),
        }
