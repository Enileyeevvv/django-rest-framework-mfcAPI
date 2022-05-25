from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers

from services.views import *

router = routers.DefaultRouter()
router.register(r'services', ServiceViewSet)

def divizionbyzero():
    result = 1 / 0

urlpatterns = [
    path('', redirect_view),
    path('admin/', admin.site.urls),
    path('api/services/filterbyq', FilterServicesByQ.as_view({'get': 'list'})),
    path('api/services/filterbysearch', FilterServicesBySearch.as_view({'get': 'list'})),
    path('api/', include(router.urls)),
    path('sentry/', divizionbyzero),
]
