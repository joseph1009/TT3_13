
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Message, User
from .forms import messageForm






@login_required(login_url='login')
def createPost(request):
    form = messageForm()
    post = Message.objects.all()
    if request.method == 'POST':
        post = request.POST.get('body')
        
        return redirect('home')

    context = {'form': form, 'post': post}
    # return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
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
    # return render(request,'file' , context)


@login_required(login_url='login')
def deletePost(request):
    post= Message.objects.get('body')

    
def search(request): #search
    template='CRUD/home.html'

    query=request.GET.get('q')

    result=Post.objects.filter(Q(title__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query))
    paginate_by=2
    context={ 'posts':result }
    return render(request,template,context)

# def deletePost(request):
def deletePost(request):
    context = {}
    return render(request, 'filenam.html',context) 


    if request.method == 'POST':
        post.delete()
        return redirect('home')
    # return render(request, 'file_name', {})

