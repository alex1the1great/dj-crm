from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('apps.accounts.urls')),

    # Local
    path('', include('apps.pages.urls', namespace='pages')),
    path('leads/', include('apps.leads.urls', namespace='leads'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
