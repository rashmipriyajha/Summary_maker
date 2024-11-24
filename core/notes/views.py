from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login/")
def notes(request):
    if request.method == "POST":
        data = request.POST

        notes_image = request.FILES.get('notes_image')
        title = data.get('title')
        summary = data.get('summary')

        Summary.objects.create(
            notes_image=notes_image,
            title=title,
            summary=summary
        )
        return redirect('/notes/')
    

    queryset = Summary.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(title__icontains = request.GET.get('search'))




    context = {'summary': queryset}
    return render(request,'notes.html',context)

@login_required(login_url="/login/")
def update_notes(request,id):
    queryset = Summary.objects.get(id=id)

    if request.method == "POST":
        data = request.POST

        notes_image = request.FILES.get('notes_image')
        title = data.get('title')
        summary = data.get('summary')

        queryset.title=title
        queryset.summary=summary

        if notes_image:
            queryset.notes_image=notes_image

        queryset.save()
        return redirect('/notes/')





    context = {'summary': queryset}
    return render(request,'update_notes.html',context)




@login_required(login_url="/login/")
def delete_notes(request,id):
    queryset = Summary.objects.get(id=id)
    queryset.delete()
    return redirect('/notes/')


def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, 'Invalid Username ')
            return redirect('/login/')
        user = authenticate(username = username , password = password)

        if user is None:
            messages.info(request, 'Invalid Password ')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/notes/')

    return render(request , 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')




def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)
        user.save()

        messages.info(request, 'Account created Successfully')


        return redirect('/register/')

    return render(request , 'register.html')

    