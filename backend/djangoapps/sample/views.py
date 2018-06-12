#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

#UTIL
import json

from django.conf import settings
from backend.djangoapps.common.views import common_sample

def sample(request):

    """
    making logic
    """

    """
    with connections['default'].cursor() as cur:
        query = '''
            select *
            FROM table
            where sample = '{page}'
        '''.format(page=page)
        cur.execute(query)
        rows = cur.fetchall()
    """

    context = {}
    context['sample_key'] = 'sample_val'

    print("-------------------------> DEBUG [s]")
    common_sample()
    print(settings.TIME_ZONE)
    print("-------------------------> DEBUG [e]")

    return render(request, 'sample/sample.html', context)
    #return JsonResponse({'a':'b'})

def vuejs(request):

    """
    making logic
    """

    """
    with connections['default'].cursor() as cur:
        query = '''
            select *
            FROM table
            where sample = '{page}'
        '''.format(page=page)
        cur.execute(query)
        rows = cur.fetchall()
    """

    context = {}
    context['sample_key'] = 'sample_val'

    print("-------------------------> DEBUG [s]")
    common_sample()
    print(settings.TIME_ZONE)
    print("-------------------------> DEBUG [e]")

    return render(request, 'sample/vuejs.html', context)
    #return JsonResponse({'a':'b'})

def vueService(request):

    """
    making logic
    """

    """
    with connections['default'].cursor() as cur:
        query = '''
            select *
            FROM table
            where sample = '{page}'
        '''.format(page=page)
        cur.execute(query)
        rows = cur.fetchall()
    """

    context = {}
    context['helloData'] = 'render data'

    print("-------------------------> DEBUG [s]")
    common_sample()
    print(settings.TIME_ZONE)
    print("-------------------------> DEBUG [e]")

    return render(request, 'sample/vueService.html', context)
    #return JsonResponse({'a':'b'})
