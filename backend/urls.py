from django.urls import path
from django.conf.urls import url

from .djangoapps.drf.views import SampleView
from .djangoapps.drf.views import SimpleUserView
from .djangoapps.drf.views import SimpleUserAddView

from .djangoapps.login import views as loginViews
from .djangoapps.sample import views as SampleViews
from .djangoapps.logout import views as logoutViews

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='happy API')

urlpatterns = [
    # rest-api

    url('api_sample$', SampleView.as_view()),
    url('api_simpleUser$', SimpleUserView.as_view()),
    url('api_simpleAddUser$', SimpleUserAddView.as_view()),

    # rest-swagger
    url('swagger$', schema_view),

    # main-url
    url('sample$', SampleViews.sample, name='sample'),
    url('vuejs$', SampleViews.vuejs, name='vuejs'),
    url('vueservice$', SampleViews.vueService, name='vueService'),

    url('login$', loginViews.login, name='login'),
    url('logout$', logoutViews.logout, name='logout'),
]
