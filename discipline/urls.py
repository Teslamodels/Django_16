from django.urls import path
from .views import Mark

urlpatterns = [
    path('', Mark.as_view(), name='mark'),
]