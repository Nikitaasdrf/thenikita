from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, timedelta
from .models import *
from .forms import *

def homePage(request):
    if request.user.is_authenticated:
        user_first_name = request.user.first_name
        user_last_name = request.user.last_name
        context = {'user_first_name': user_first_name, 'user_last_name': user_last_name, 'footertitle': 'Главная страница',}
    else:
        context = {'footertitle': 'Главная страница',}
    return render(request, 'mainApp/homePage.html', context)

def blog(request):
    if request.user.is_authenticated:
        user_first_name = request.user.first_name
        user_last_name = request.user.last_name
        blog = Blog.objects.order_by('-posted')
        context = {'user_first_name': user_first_name, 'user_last_name': user_last_name, 'footertitle': 'Блог', 'blog': blog}
    else:
        blog = Blog.objects.all()
        context = {'footertitle': 'Блог', 'blog': blog}
    return render(request, 'mainApp/blog.html', context)

def useres(request):
    if request.user.is_authenticated:
        user_first_name = request.user.first_name
        user_last_name = request.user.last_name
        context = {'user_first_name': user_first_name, 'user_last_name': user_last_name, 'footertitle': 'Полезные ресурсы',}
    else:
        context = {'footertitle': 'Полезные ресурсы',}
    return render(request, 'mainApp/useres.html', context)
    
def video(request):
    if request.user.is_authenticated:
        user_first_name = request.user.first_name
        user_last_name = request.user.last_name
        context = {'user_first_name': user_first_name, 'user_last_name': user_last_name, 'footertitle': 'Видео',}
    else:
        context = {'footertitle': 'Видео',}
    return render(request, 'mainApp/video.html', context)
    
def feedback(request):
    data = None
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['message'] = form.cleaned_data['message']
            data['email'] = form.cleaned_data['email']
            form.save()
            form = None
    else:
        form = MessageForm()
    context = {'form': form, 'data': data, 'footertitle': 'Обратная связь',}
    return render(request, 'mainApp/feedback.html', context)

def contacts(request):
    if request.user.is_authenticated:
        user_first_name = request.user.first_name
        user_last_name = request.user.last_name
        context = {'user_first_name': user_first_name, 'user_last_name': user_last_name, 'footertitle': 'Контакты',}
    else:
        context = {'footertitle': 'Контакты',}
    return render(request, 'mainApp/contacts.html', context)

def about(request):
    if request.user.is_authenticated:
        user_first_name = request.user.first_name
        user_last_name = request.user.last_name
        context = {'user_first_name': user_first_name, 'user_last_name': user_last_name, 'footertitle': 'О нас',}
    else:
        context = {'footertitle': 'О нас',}
    return render(request, 'mainApp/about.html', context)

def addarticle(request):
    formmessage = Message.objects.all()
    if request.user.is_superuser:
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid() and form.cleaned_data['picture'] != None:
                form.save()
                form = BlogForm()
            else:
                form.add_error(None, "Заполните все поля!")
        else:
            form = BlogForm()
        context = {'footertitle': 'Добавть статью', 'form': form, 'formmessage': formmessage}
    else:
        context = {'formmessage': formmessage}
        return redirect('homePage')
    return render(request, 'mainApp/addarticle.html', context)

def blogcontent(request, pk):
    post = Blog.objects.get(id=pk)
    comment = Comment.objects.filter(post = pk).order_by('-time')
    if request.user.is_authenticated:
        user_first_name = request.user.first_name
        user_last_name = request.user.last_name
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form2 = form.save(commit=False)
                form2.user = request.user
                form2.time = datetime.now()
                form2.post = post
                form2.save()
                form = CommentForm()
        else:
            form = CommentForm()
        context = {'user_first_name': user_first_name, 'user_last_name': user_last_name, 'footertitle': 'Блог', 'form': form, 'post': post, 'comment': comment}
    else:
        context = {'post': post}
    return render(request, 'mainApp/blogcontent.html', context)