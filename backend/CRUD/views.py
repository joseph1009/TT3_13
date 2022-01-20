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

def search(request):
    template='CRUD/home.html'

    query=request.GET.get('q')

    result=Post.objects.filter(Q(title__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query))
    paginate_by=2
    context={ 'posts':result }
    return render(request,template,context)

# def deletePost(request):


