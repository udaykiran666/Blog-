from rest_framework.routers import DefaultRouter
from blog_app import views, urls

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'blogs', views.BlogViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = router.urls + urls.urlpatterns
