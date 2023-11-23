from django.urls import include, path

from app3 import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
   path('api-auth/', include('rest_framework.urls')),
   path('createaccount',views.createaccount.as_view(),name='create'),
   path('auth_login',views.auth_login.as_view(),name='auth_login')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)