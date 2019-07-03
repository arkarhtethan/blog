from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path('',views.BlogHome.as_view(), name="home")
]