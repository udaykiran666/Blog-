from rest_framework.routers import DefaultRouter
from blog_app import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = router.urls
