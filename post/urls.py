from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path('',views.BlogHome.as_view(), name="home"),
    path('search/',views.SearchView.as_view(), name="search"),
    path('share/<int:pk>/',views.share_post_view, name="share"),
    path('detail/<slug:slug>/',views.PostDetailView.as_view(), name="detail"),
]