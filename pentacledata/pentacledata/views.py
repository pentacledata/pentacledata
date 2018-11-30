from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.db.models import Count, Sum
from django.db.models.functions import ExtractMonth, ExtractYear
from django.http import Http404, JsonResponse
from django.forms.formsets import formset_factory
from pentacledata.forms import PatientDetails
from pentacledata.models import Patient
from django import db

# import python libs
import json
import logging
import datetime
import time
import sys
import requests
from collections import OrderedDict
from itertools import groupby
import threading
logger = logging.getLogger(__name__)


@csrf_exempt
def generate_home_page(request):
    if request.method == 'GET':
        return render(request, 'home.html', {
            'component_data': "Anil Kumar G"})


def home(request):
    form_patient = PatientDetails()

    patient_details = {}

    patient_details = Patient.objects.all()

    if request.method == 'GET':
        form_patient = PatientDetails()
    elif request.method == 'POST':
        form_patient = PatientDetails(request.POST)
        if form_patient.is_valid():
            patient_name = form_patient.cleaned_data['patient_name']
            mobile = form_patient.cleaned_data['mobile']
            print("Before")
            try:
                created = Patient.objects.create(
                    patient_name=patient_name,
                    mobile=mobile
                )
            except Exception as e:
                print("The exceptions is " + str(e))
    return render(request, 'home.html',
                  {
                   'form_patient': form_patient,
                   'patient_details': patient_details
                   })


