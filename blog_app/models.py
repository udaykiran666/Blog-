import uuid
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    uuid =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(max_length=1024, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    written_by = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', related_name='blogs')

    def __str__(self):
        return self.title
    
class Category(models.Model):
    uuid =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    uuid =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(max_length=1024, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
# Create your models here.
