from django.conf.urls import url, include

from .views import (
    StatusAPIView,
    StatusAPIDetailView,
    # StatusDetailAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView,
)


urlpatterns = [
    url(r'^$', StatusAPIView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view(), name='detail'),
]