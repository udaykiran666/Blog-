from django.shortcuts import render
from blog_app.serializers import *
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer
