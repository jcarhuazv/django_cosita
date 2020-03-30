from django.urls import path
from posts import views

urlpatterns = [
    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='posts_feed',
    ),
    path(
        route='create/',
        view=views.PostsCreateView.as_view(),
        name='posts_create',
    ),
    path(
        route='<int:pk>/update/',
        view=views.PostsUpdateView.as_view(),
        name='posts_update',
    ),
    path(
        route='<int:pk>/delete/',
        view=views.PostsDeleteView.as_view(),
        name='posts_delete',
    ),
]
