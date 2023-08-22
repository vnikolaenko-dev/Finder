import datetime

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *


# Исполнитель about
def index(request):
    return render(request, 'main/index.html')


# Исполнитель projects
def projects(request):
    tasks = Project.objects.all()
    for i in tasks:
        print(i)
    # tasks = Task.objects.order_by('-id'[:5])
    return render(request, 'main/projects.html', {'title': 'Главная страница', 'tasks': tasks})


# Исполнитель about
def profile(request, user_id=None):
    try:
        if user_id == request.session['user'] or user_id is None:
            name = User.objects.filter(email=request.session['user']).first().name
            image = User.objects.filter(email=request.session['user']).first().image
            tasks = Text.objects.filter(email=request.session['user']).all()[::-1]
            return render(request, 'main/profile_owner.html', {'name': name, 'image': image, 'tasks': tasks})
        else:
            name = User.objects.filter(email=user_id).first().name
            image = User.objects.filter(email=user_id).first().image
            tasks = Text.objects.filter(email=user_id).all()[::-1]
            return render(request, 'main/profile.html', {'name': name, 'image': image, 'tasks': tasks, 'email': user_id})
    except KeyError:
        return redirect('/login')


# Исполнитель project
def project(request, project_id):
    task = Project.objects.filter(id=int(project_id))
    return render(request, 'main/project.html', {'task': task})


# Исполнитель create
def create(request):
    error = ''
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была заполнена неверно'

    form = ProjectForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


# Исполнитель create
def create_note(request):
    error = ''
    if request.method == 'POST':
        form = TextForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.email = User.objects.filter(email=request.session['user']).first().email
            instance.sent = datetime.now().date()

            instance.save()
            return redirect('/profile')
        else:
            error = 'Форма была заполнена неверно'

    form = TextForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_note.html', context)


# Исполнитель login
def login(request):
    error = ''
    try:
        if request.method == 'POST':
            form = UserForm(request.POST,  request.FILES)
            form.save()
            if form.is_valid():
                form.save()
                img_obj = form.instance
                request.session['user'] = form.data['email']
                return redirect('/')
            else:
                error = 'Форма была заполнена неверно'
    except ValueError:
        error = 'Данная почта уже зарегистрирована'

    form = UserForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/login.html', context)


# Исполнитель signup
def signup(request):
    error = ''
    if request.method == 'POST':
        form = UserFormOpen(request.POST)
        if form.is_valid():
            code_instance = User.objects.filter(email=form.data['email'], password=form.data['password']).first()
            if code_instance:
                # Передача значения в сессию
                request.session['user'] = form.data['email']
                return redirect('/profile/' + request.session['user'])
            else:
                error = 'Проверьте логин или пароль'
        else:
            error = 'Форма была заполнена неверно'

    form = UserFormOpen()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/signup.html', context)


def subscriptions(request):
    if request.method == 'POST':
        search = dict(request.POST)['search']
        context = User.objects.filter(name=search[0])
        return render(request, 'main/subscriptions.html', {'context': context})
    context = User.objects.all()
    return render(request, 'main/subscriptions.html', {'context': context})

