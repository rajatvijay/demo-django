from django.conf.urls import url
from blog.views import PostListView, CreatePostView

urlpatterns = [
    url('^list', PostListView.as_view()),
    url('^create', CreatePostView.as_view())
]
