from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def image_list(request):
    images = Image.objects.all()
    return render(request, 'newapp/image_list.html', {'images': images})

@login_required(login_url="login")
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'newapp/upload_image.html', {'form': form})

def login_user(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('/')
                           
    
    return render(request, 'newapp/login.html', {'form':form})

def logout_user(request):
    logout(request)
    return redirect('/login')
    






