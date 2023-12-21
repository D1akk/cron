from django.urls import path
from .views import (
    Login,
    ListCreateNote
)
from django.contrib.auth.views import LogoutView;

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('list-create-note/', ListCreateNote.as_view(), name='list-create-note')
]