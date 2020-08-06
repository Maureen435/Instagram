from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import ImageForm,ProfileForm,CommentsForm
from django.contrib.auth import login 

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()
    comments = Comments.objects.all()
    return render(request, 'instagram/index.html', {"images":images,"comments":comments})
    