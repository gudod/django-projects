from django.urls import path
from .views import PostDeleteView, PostListView, PostDetailView, PostCreateView, PostUpdateView
from . import views

urlpatterns = [
    #path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('about/', views.about, name='blog-about'),
]
