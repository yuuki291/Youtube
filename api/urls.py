from rest_framework.routers import DefaultRouter
from django.urls import path
from django.conf.urls import include
from .views import VideoViewSet, CreateUserView, ProfileViewSet, MessageViewSet, InboxListView
from api import views
app_name = 'api'

router = DefaultRouter()
router.register('videos', VideoViewSet)
router.register('profile', ProfileViewSet)
router.register('approval', views.FriendRequestViewSet)
router.register('message', MessageViewSet, basename="message")
router.register('inbox', InboxListView, basename="inbox")


urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('myprofile/', CreateUserView.as_view(), name='myprofile'),
    path('', include(router.urls)),
]
