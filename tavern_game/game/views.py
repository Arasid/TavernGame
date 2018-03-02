import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count

from .models import RichPerson
from .forms import RichPersonForm

def index(request):
    return render(request, 'game/index.html', {})

def rich_people(request):
    rich_people = RichPerson.objects.order_by('-value')

    context_dict = {
        'rich_people': rich_people,
    }
    return render(request, 'game/rich_people.html', context_dict)


@login_required
@staff_member_required
def rich_fortune(request):
    if request.method == 'POST':
        form = RichPersonForm(request.POST)
        if form.is_valid():
            person = form.cleaned_data.get('person')
            value = form.cleaned_data.get('value')

            rich = RichPerson.objects.filter(person=person).first()
            if rich is None:
                rich = RichPerson.objects.create(
                        person=person,
                        value=value)
            else:
                rich.value = value
                rich.save()

            return redirect('rich_fortune')
    else:
        form = RichPersonForm()
    context_dict = {
        'form': form,
    }
    return render(request, 'game/rich_fortune.html', context_dict)

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')
