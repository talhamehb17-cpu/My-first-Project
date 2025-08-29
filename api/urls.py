# api/urls.py
from django.urls import path, include

urlpatterns = [
    path('project/', include('api.controllers.Project.urls')),  # ✅ full path
]
