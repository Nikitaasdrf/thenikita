from django import forms
from .models import *
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput, FileInput, SplitDateTimeWidget

class MessageForm(ModelForm):
   class Meta:
      model = Message
      fields = ["name", "message", "ans", "email",]
      widgets = {
         "name": TextInput(attrs={'placeholder': 'Введите имя',}),
         "message": Textarea(attrs={'placeholder': 'Введите ваше сообщение'}),
         "ans": CheckboxInput(attrs={'name': 'scales', 'id': 'scales', 'style': 'height: 1rem;', 'checked': ''}),
         "email": TextInput(attrs={'placeholder': 'Введите e-mail'})
      }

class BlogForm(ModelForm):
   class Meta:
      model = Blog
      fields = ["picture", "title", "description", "content", "posted",]
      widgets = {
         "picture": FileInput(attrs={'style': 'margin: 0.5rem auto;'}),
         "title": TextInput(attrs={'placeholder': 'Заголовок', 'class': 'title-class',}),
         "description": TextInput(attrs={'placeholder': 'Краткое содержание', 'class': 'title-class',}),
         "content": Textarea(attrs={'placeholder': 'Полное содержание', 'class': 'text-class',}),
         "posted": TextInput(attrs={'class': 'time-class', 'type':'datetime-local'})
      }

class CommentForm(ModelForm):
   class Meta:
      model = Comment
      fields = ["comment"]
      widgets = {
         "comment": Textarea(attrs={'placeholder': 'Добавить комментарий'})
      }