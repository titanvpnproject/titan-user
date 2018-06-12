#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

#REST-API
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import SampleSerializer
from .serializers import SimpleUserSerializer

#UTIL
import json

class SampleView(CreateAPIView):

    serializer_class = SampleSerializer

    def create(self, request):

        id = request.POST.get('id')
        print("id = ", id)

        return Response({"result": "ok"})

class SimpleUserView(CreateAPIView):

    serializer_class = SimpleUserSerializer

    def create(self, request):

        with connections['default'].cursor() as cur:
            query = '''
                select email, regist_date
                from sample_user
            '''
            cur.execute(query)
            rows = cur.fetchall()

        return Response({"result": rows})
