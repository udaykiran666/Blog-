from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog_app import views

from django.urls import path

urlpatterns = [
    path('<uuid:uuid>/comments/', views.CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('tag_cloud/', views.TagCloudViewSet.as_view(), name='tags_cloud'),
    path('tag_cloud/<uuid:uuid>/', views.TagCloudViewSet.as_view(), name='tags_cloud_detial'),
]
