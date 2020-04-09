from django.shortcuts import render
from .models import Article

def index(req):
    context = {

    }
    return render(req, 'index.html', context=context)