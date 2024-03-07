from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("add_post", views.add_post, name="add-post"),
    path("save_post", views.save_post, name="save_post"),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail,
         name="post-detail-page")  # /posts/my-first-post
]