from django.urls import path, include
from rest_framework import routers
from .models import *
from .views import *

router = routers.DefaultRouter()
router.register(r'users', APIViewSet)

urlpatterns = [
    path('', home),
    path('api/', include(router.urls)),
    path('post/<str:name>/<int:phone>/<str:email>/<str:location>/',emergency)
]