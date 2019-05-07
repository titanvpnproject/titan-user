import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections


def sample(request):

    context = {}
    context['sample_key'] = 'sample_val'

    return render(request, 'ios/aaa.html', context)
