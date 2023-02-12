from django.urls import re_path
from algo_tracker import views

urlpatterns = [
    re_path(r'^question$', views.questionApi),
    re_path(r'^user$', views.userApi)
    # re_path(r'^question/(?P<pk>[0-9]+)$', views.questionApi),
]