from django.conf.urls import url

from .views import (
            UpdateModelAPIView,
            UpdateModelListAPIView,
    )

urlpatterns = [
    url(r'^$', UpdateModelListAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', UpdateModelAPIView.as_view()),
]