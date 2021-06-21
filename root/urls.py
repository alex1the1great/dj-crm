from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from apps.leads.views import LandingPage

urlpatterns = [
    path('admin/', admin.site.urls),

    # Local
    path('', LandingPage.as_view(), name='landing_page'),
    path('leads/', include('apps.leads.urls', namespace='leads'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
