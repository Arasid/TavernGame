import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count

def index(request):
    return render(request, 'game/index.html', {})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')
