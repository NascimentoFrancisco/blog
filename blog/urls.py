from django.urls import path
from blog.views import ListPostsView, DetailPostView

app_name = "posts"

urlpatterns = [
    path('', ListPostsView.as_view(), name='list'),
    path('post/<int:pk>/', DetailPostView.as_view(), name='detail'),
]
