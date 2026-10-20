from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("investo-centre/", views.investo_centre, name="investo_centre"),
    path("contact/", views.contact, name="contact"),
    path("blogs/", views.blogs, name="blogs"),
    path("join-us/", views.join_us, name="join_us"),
]