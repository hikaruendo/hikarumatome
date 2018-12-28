from django.urls import path
from . import views
from .views import PostListView
from .views import PostDetailView
from .views import PostCreateView
from .views import PostUpdateView
from .views import PostDeleteView
from .views import UserPostListView
from work.views import IndexView
from rest.views import rest

urlpatterns = [
    path('', PostListView.as_view(), name='write-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),   
    path('work/', IndexView.as_view(), name='index'),   
    path('rest/', rest, name='rest'),   

]