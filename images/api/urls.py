from django.urls import path, include
from rest_framework import routers
from .views import ImageViewSet

router = routers.DefaultRouter()
router.register('images', ImageViewSet)

app_name = 'api-images'
urlpatterns = [
    path(r'', include(router.urls)),
]