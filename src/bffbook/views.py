from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    user = request.user
    context  = { }
    context['user'] = user
    return render(request,"main/home.html" , context)