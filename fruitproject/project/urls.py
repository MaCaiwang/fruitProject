from django.conf.urls import url
import views

urlPatterns = [
    url(r'^', views.login)
]
