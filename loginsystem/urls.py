"""loginsystem URL Configuration

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
from django.urls import path
from signin import views as signin_views
from register import views as register_views
from . import views, settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', signin_views.signin, name='signin'),
    path('signin/successful/', signin_views.auth_user, name='auth_user'),
    path('logout/', signin_views.logout, name='logout'),
    path('register/', register_views.register, name='register'),
    path('register/successful', register_views.db_register, name='db_register'),
    path('register/successpg', register_views.success_register_page, name='success_pg'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
