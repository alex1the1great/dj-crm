from django.contrib import admin

from .models import Lead, Agent, UserProfile

admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(UserProfile)
