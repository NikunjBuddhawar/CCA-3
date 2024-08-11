from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import work
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

@login_required
def home(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = TaskForm()

    all_items = work.objects.all()
       
    return render(request, 'index.html', {'form': form, 'all_items': all_items, 'username': request.user.username})

def delete(request, list_id):
    item = get_object_or_404(work, pk=list_id)  
    item.delete()
    return redirect('home')


def toggle(request,list_id):
    item = work.objects.get(pk=list_id)
    item.status = not item.status 
    item.save()
    return redirect('home') 

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, "Error: " + str(form.errors))
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def logout(request):
    return redirect('login')

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid login credentials")  
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def edit(request, list_id):
    item = get_object_or_404(work, pk=list_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=item)

    return render(request, 'edit.html', {'form': form, 'item': item})