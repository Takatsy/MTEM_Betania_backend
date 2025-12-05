from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from api.views import ViewMpikambana, ViewSampana

route = routers.DefaultRouter()

route.register("mpikambana", ViewMpikambana, basename='viewmpikambana')
route.register("sampana", ViewSampana, basename='viewsampana')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
