from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path('',views.BlogHome.as_view(), name="home"),
    path('search/',views.SearchView.as_view(), name="search"),
    path('search/tag/',views.SearchSimilarTag.as_view(), name="search-tag"),
    path('contact/',views.ContactView.as_view(), name="contact"),
    path('share/<int:pk>/',views.share_post_view, name="share"),
    path('detail/<slug:slug>/',views.PostDetailView.as_view(), name="detail"),
    path('add-comment/<slug:slug>/',views.post_comment, name="add_comment"),
]