from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djreact.apps.authentication.urls')),
    path('', include('djreact.apps.core.urls'))
]
