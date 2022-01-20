from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def home(request):
    return HttpResponse("Hi")

def editPost(request):
    post =  Post.objects.all
    context = {}
    return render(request,'filename.html',context)

def deletePost(request):
    context = {}
    return render(request, 'filenam.html',context) 


