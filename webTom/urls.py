"""
URL configuration for webTom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from core import views  # type: ignore
from accounts import views as accounts_views # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', accounts_views.loginPage, name = "login"),
    path('register/', accounts_views.registerPage, name = "register"),
    path('logout/', accounts_views.logoutUser, name = "logout"),
    path('home/', accounts_views.home, name = "home"),
    path('', views.home, name = "index")
]
