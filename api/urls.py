from rest_framework.routers import DefaultRouter
from django.urls import path
from django.conf.urls import include
from .views import VideoViewSet
app_name = 'api'

router = DefaultRouter()
router.register('videos', VideoViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
