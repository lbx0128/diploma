from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    user = models.User.objects.get(pk=1)
    return render(request,'index.html',{'user':user})