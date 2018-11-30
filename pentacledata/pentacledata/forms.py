from django import forms
from django.forms import formset_factory
from django.forms.formsets import BaseFormSet
from django.forms.fields import DateField
from django.core.validators import RegexValidator
from pentacledata.models import *
import datetime
from django.utils import timezone


class PatientDetails(forms.Form):

    first_name = forms.CharField(label='Patient First Name', required=True,widget=forms.TextInput(
                                         attrs={'size': '20', 'placeholder': 'First Name'}), max_length=20)

    last_name = forms.CharField(label='Patient Last Name', required=True,widget=forms.TextInput(
                                         attrs={'size': '30', 'placeholder': 'Last Name'}), max_length=20)

    middle_name = forms.CharField(label='Patient Middle Name', required=True,widget=forms.TextInput(
                                         attrs={'size': '30', 'placeholder': 'Middle Name'}), max_length=20)




