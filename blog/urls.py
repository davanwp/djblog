from django.urls import path
from blog import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("contact/", views.contact.as_view(), name="contact"),
    path("about-us/", views.about.as_view(), name="about"),
]