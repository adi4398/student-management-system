
from django.contrib import admin
from django.urls import path ,include
from mytodolist import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('listapp.urls')), # Linking the app/urls.py with the project urls.
    path('events/', include('events.urls')),   
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
