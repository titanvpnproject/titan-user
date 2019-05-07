from django.urls import path
from django.conf.urls import url

from .djangoapps.sample import views as SampleViews

from .djangoapps.android.rest_api import views as AndroidRestApiViews
from .djangoapps.android.webview import views as AndroidWebviewViews

from .djangoapps.ios.rest_api import views as IOSRestApiViews
from .djangoapps.ios.webview import views as IOSRestApiWebviewViews

urlpatterns = [
    path('', SampleViews.sample, name='sample'),

    path('api/v1/android', AndroidRestApiViews.sample, name='sample'),
    path('webview/v1/android', AndroidWebviewViews.sample, name='sample'),

    path('api/v1/ios', IOSRestApiViews.sample, name='sample'),
    path('webview/v1/ios', IOSRestApiWebviewViews.sample, name='sample'),

    # how to connect / use browser below url

    # http://<host>:<port>/api/v1/android
    # http://<host>:<port>/webview/v1/android
    # http://<host>:<port>/api/v1/ios
    # http://<host>:<port>/webview/v1/ios
]
