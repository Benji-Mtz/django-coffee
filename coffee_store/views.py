from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from django.contrib.auth.models import User

from .forms import RegisterForm

""" def index(request):
    return HttpResponse('Hola Desde views.py!') """
    
def index(request):
    return render(request, 'index.html', {
        # context
        'message': 'Listado de productos',
        'titulo': 'Productos',
        'products' : [
            {'title':'Playera', 'price': 5, 'stock': True},
            {'title':'Camisa', 'price': 15, 'stock': True},
            {'title':'Mochila', 'price': 52, 'stock': False},
        ]
    })

def login_view(request):
    # print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username') #diccionario post metodo get
        password = request.POST.get('password') 
        
        # print(username,"\n", password)
        user = authenticate(username=username, password=password) #None
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o Contraseña no Validos')
        
    return render(request, 'users/login.html', {
        # context
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login')

def register(request):
    #  RegisterForm({diccionario para colocar valores por default})
    form = RegisterForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        ''' username = form.cleaned_data['username'] 
        email = form.cleaned_data.get('email')    
        password = form.cleaned_data.get('password') '''
        
        # print(f'username: {username},email: {email},password: {password},')
        # user = User.objects.create_user(username, email, password)
        
        user = form.save()
        
        if user:
            login(request, user)
            messages.success(request, 'El usuario {} se creo con exito'.format(user.username))
            return redirect('index')
       
    return render(request, 'users/register.html', {
        'form': form
    })