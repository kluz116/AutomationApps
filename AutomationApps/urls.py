
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from AutomationApps.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('LegalDoc/', include('LegalDoc.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('todo_api/', include('todo_api.urls')),
    path('Crm/', include('Crm.urls')),
    path('Metropol/', include('Metropol.urls')),
    path('innovations/', include('innovations.urls')),
    path("api/", api.urls),  # <---------- !

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)