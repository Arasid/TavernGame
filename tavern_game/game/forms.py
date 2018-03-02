from django import forms
from django.db.models import Q

from game.models import Person, Ration, BarPurchase, RichPerson


class RichPersonForm(forms.Form):
    person = forms.ModelChoiceField(
            queryset=Person.objects.all(),
            widget=forms.Select(),
            empty_label=None,
    )
    value = forms.IntegerField(min_value=1)
