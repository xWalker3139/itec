from django.conf.urls import url
from my_app import views

app_name = "my_app"

urlpatterns = [
    url(r'^login_user/$', views.login_user, name="login_user"),
]