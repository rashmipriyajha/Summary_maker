from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):

    peoples = [
        {'name': 'Rashmi', 'age': 24},
        {'name': 'Rohan', 'age': 6},
        {'name': 'Deepanshu', 'age': 13},
        {'name': 'Neha', 'age': 22}
    ]

    for people in peoples:
        if people['age'] : 10
        print("Yes")
    
    vegetables = ['Pumpkin', 'Tomato', 'Potato']



    return render(request,"index.html",context={'page' : 'Django Tutorial','peoples': peoples,'vegetables':vegetables})
    
def about(request):
    context = {'page': 'About'}
    return render(request,"about.html",context)

def contact(request):
    context = {'page': 'Contact'}
    return render(request,"contact.html",context)

def success_page(request):
    print("*"*10)
   
    return HttpResponse("<h1>This is a success page.</h1>")