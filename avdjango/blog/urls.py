from django.conf.urls import url
from blog.views import PostListView

urlpatterns = [
    url('^list', PostListView.as_view())
]
