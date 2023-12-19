from django.urls import path
from .views import (
    Login,
    ListCreateNote
)

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('list-create-note/', ListCreateNote.as_view(), name='list-create-note')
]