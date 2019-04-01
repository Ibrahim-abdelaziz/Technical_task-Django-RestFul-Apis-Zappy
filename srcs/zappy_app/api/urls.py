from django.contrib import admin
from django.urls import path, include

from zappy_app.views import send_data
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('zappy_app',views.PostView)

urlpatterns = [
    path('', include(router.urls)),
    path('',views.PostView),
    path('send/',send_data),
]
