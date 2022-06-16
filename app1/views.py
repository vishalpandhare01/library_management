from django.shortcuts import redirect, render ,HttpResponse
from django.contrib.auth import authenticate, login,logout
from .models import library
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    li=library.objects.all()
    data={
        'li':li
    }
    return render(request,'index.html',data)

# 'book_name','author_name','book_desc'
def add(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        author_name = request.POST.get('author_name')
        book_desc = request.POST.get('book_desc')
        book_add = library(book_name=book_name,author_name=author_name,book_desc=book_desc)
        book_add.save()
        return redirect('/')
    return render(request,'add.html')    

def remove_book(request,book_id=0):
    if request.method == 'POST':
        l=library.objects.get(id=book_id)
        l.delete()
        return redirect('/')
    return render(request,'delete.html')

def new_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')

        user= User.objects.create_user(username=username,email=email,password=password)
        user.first_name = first_name
        user.save()
        return redirect('LogIn')
    return render(request,'authentication/reg.html')

def LogIn(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = authenticate(password=password,username=username)
        if user is not None:       
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('login invalid.........')
    return render(request,'authentication/login.html')

def LogOut(request):
    logout(request)
    return redirect('/')