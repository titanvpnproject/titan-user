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
from .serializers import SimpleUserAddSerializer

#UTIL
import json

from backend.djangoapps.common.views import dictfetchall

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
                select
                    id,
                    email,
                    DATE_FORMAT(regist_date,'%Y-%c-%e') as regist_date
                from sample_user
            '''
            cur.execute(query)
            #rows = cur.fetchall()
            rows = dictfetchall(cur)

        print(rows)

        return Response({"result": rows})

class SimpleUserAddView(CreateAPIView):

    serializer_class = SimpleUserAddSerializer

    def create(self, request):

        jsonData = json.loads(request.body.decode('utf-8'))

        email = jsonData['email']
        password = jsonData['password']

        with connections['default'].cursor() as cur:
            query = '''
                insert into sample_user(email, password)
                value ('{email}', '{password}');
            '''.format(email=email, password=password)
            cur.execute(query)

        return Response({"result": "success"})
