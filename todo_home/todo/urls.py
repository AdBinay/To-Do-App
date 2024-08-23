from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet
from . import views

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
]
