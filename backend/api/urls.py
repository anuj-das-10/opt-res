from django.urls import path
from .views import optimize_resume

urlpatterns = [
    path('optimize-resume/', optimize_resume, name='optimize_resume'),
]
