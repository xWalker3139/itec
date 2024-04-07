"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
from my_app import views

app_name = "my_app"

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'my_app/', include("my_app.urls", namespace='my_app')),
    url(r"^home/$", views.home, name="home"),
    url(r"^logout_user/$", views.logout_user, name="logout"),
    url(r'^account/$', views.account, name="account"),
    url(r"^inregistrare/$", views.inregistrare_user, name="inregistrare"),
    url(r"^register_app/$", views.register_app, name="register_name"),
    url(r"^register_endpoint/(?P<pk>\d+)/$", views.register_endpoint, name="register_endpoint"),
    url(r'^dashboard/(?P<pk>\d+)/$', views.raportare_bug, name="raportare_bug"),
    url(r'^dashboard_dev/$', views.dashboard_dezvoltator, name="dashboard_dev"),
    url(r'^status/(?P<pk>\d+)/$', views.status, name="status"),
    url(r'^editare_setari/$', views.editare_setari, name="editare_setari"),
]
