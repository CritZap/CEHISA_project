from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from index.models import Menu

def menus(request):
    menus = Menu.objects.all()
    return render(request, 'index.html', locals())

