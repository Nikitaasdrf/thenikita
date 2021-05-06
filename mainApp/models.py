from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

class Blog(models.Model):
    picture = models.ImageField(null=True, blank=True, upload_to="")
    title = models.CharField('Сообщение', max_length=50)
    description = models.CharField("Краткое содержание", max_length=150)
    content = models.TextField("Полное содержание")
    posted = models.DateTimeField("Время", default=datetime.now)
    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField('Имя', max_length=50)
    message = models.TextField('Сообщение')
    ans = models.BooleanField('Отправить ответ на e-mail')
    email = models.CharField('E-mail', max_length=50)
    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    comment = models.TextField('Сообщение')
    time = models.DateTimeField("Время", default=datetime.now)
    post = models.ForeignKey(Blog, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.user