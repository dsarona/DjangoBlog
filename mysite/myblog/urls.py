from django.conf.urls import url
from .views import stub_view
from .views import list_view
from .views import detail_view

urlpatterns = [
    url('', list_view, name="blog_index"),
    url('posts/(\d+)/$', detail_view, name="blog_detail"),
]