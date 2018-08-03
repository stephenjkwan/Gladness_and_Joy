from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.template import loader


def index(request):
    users_list=User.objects.all()
   # template = loader.get_template('../templates/index.html')
    return render(request,
            'dashboard/index.html',
            context={'users_list':users_list})
    #return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
