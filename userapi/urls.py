from django.urls import path
from users.views import create_user, login, select_all_users, home

urlpatterns = [
    path('', home, name='home'),
    path('create-user/', create_user, name='create_user'),
    path('login/', login, name='login'),
    path('select-all-users/', select_all_users, name='select_all_users'),
]
