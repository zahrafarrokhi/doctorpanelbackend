from django.urls import include, path
from rest_framework import routers

from doctor import views

router = routers.DefaultRouter()
router.register(r'doctor', views.DoctorsViewSet,
                basename='doctors')
urlpatterns = [
    path('', include(router.urls)),
]