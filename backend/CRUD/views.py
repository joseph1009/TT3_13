
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Message, User
from .forms import messageForm

def home(request):
    context = {}
    return render (request,'CRUD/home.html',context)


@login_required
def createPost(request):
    form = messageForm()
    post = Message.objects.all()
    if request.method == 'POST':
        post = request.POST.get('body')
        
        return redirect('home')

    context = {'form': form, 'post': post}
    return render(request,'CRUD/post.html' , context)


@login_required
def updatePost(request):
    user= User.objects.get(name=request.user)
    form = messageForm()
    post = Message.objects.all()
    if request.user != Message.user:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        post = request.POST.get('body')
        post.user = request.POST.get('user')
       
        post.save()
        return redirect('home')

    context = {'form': form, 'post': post}
    return render(request,'CRUD/post.html' , context)


@login_required
def deletePost(request):
    post= Message.objects.get('body')

    if request.user != post.user:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'CRUD/delete.html', {'obj': post})

