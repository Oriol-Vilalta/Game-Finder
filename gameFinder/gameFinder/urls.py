"""gameFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gamefinder.views import home, addGame, deleteGame, updateGame, register, login_view, logout_view, gameDetail, not_found

urlpatterns = [
    # path('default', not_found, name='not_found'),
    path('', home, name='home'),
    path('home/', home, name='home'),

    path('home/addGame/', addGame, name='addgame'),
    path('admin/', admin.site.urls),
    path('deleteGame/<int:id_game>/', deleteGame, name='deletegame'),
    path('updateGame/<int:id_game>/', updateGame, name='updategame'),
    path('gameDetail/<int:id_game>/', gameDetail, name='gamedetail'),

    path('register/', register, name='register'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),


    # path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

]
handler404 = not_found
