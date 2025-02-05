from django.urls import path, include
from . import views

urlpatterns = [
    path("blogPosts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("blogPosts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name="update"),
    path("BlogPostList/", views.BlogPostList.as_view(), name="view_blogposts")
]