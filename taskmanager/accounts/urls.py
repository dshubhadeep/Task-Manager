from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('home/', views.home_view, name="home"),
    path('logout/', views.logout_view, name="logout"),
    path('create_team/', views.create_team, name="create_team")
]
