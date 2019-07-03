from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path('',views.BlogHome.as_view(), name="home"),
    path('detail/<slug:slug>/',views.PostDetailView.as_view(), name="detail"),
]