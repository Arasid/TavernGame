import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Sum

from .models import Ration, BarPurchase, RichPerson
from .forms import AddRationsForm, AddBarPurchaseForm, RichPersonForm

def index(request):
    return render(request, 'game/index.html', {})

def rations(request):
    ration_people = Ration.objects.values('person', 'person__name').annotate(sum=Sum('value')).order_by('-sum')

    context_dict = {
        'ration_people': ration_people,
    }
    return render(request, 'game/rations.html', context_dict)

@login_required
@staff_member_required
def add_rations(request):
    if request.method == 'POST':
        form = AddRationsForm(request.POST)
        if form.is_valid():
            person = form.cleaned_data.get('person')
            value = form.cleaned_data.get('value')

            request.session['last_value'] = value

            for p in person:
                rich = Ration.objects.create(
                        person=p,
                        value=value)

            return redirect('add_rations')
    else:
        if request.session.get('last_value', 0):
            form = AddRationsForm(initial={'value': request.session.get('last_value')})
        else:
            form = AddRationsForm()
    context_dict = {
        'form': form,
    }
    return render(request, 'game/add_rations.html', context_dict)

def bar_purchases(request):
    bar_people = BarPurchase.objects.values('person', 'person__name').annotate(sum=Sum('value')).order_by('-sum')

    context_dict = {
        'bar_people': bar_people,
    }
    return render(request, 'game/bar_purchases.html', context_dict)

@login_required
@staff_member_required
def add_bar_purchase(request):
    if request.method == 'POST':
        form = AddBarPurchaseForm(request.POST)
        if form.is_valid():
            person = form.cleaned_data.get('person')
            value = form.cleaned_data.get('value')

            rich = BarPurchase.objects.create(
                    person=person,
                    value=value)

            return redirect('add_bar_purchase')
    else:
        form = AddBarPurchaseForm()
    context_dict = {
        'form': form,
    }
    return render(request, 'game/add_bar_purchase.html', context_dict)

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
