from django.shortcuts import render
from .models import UserCredential

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = UserCredential(username=username, password=password)
        user.save()
        
    return render(request, 'master_app/login.html')

def index(request):
    return render(request, 'master_app/index.html')
