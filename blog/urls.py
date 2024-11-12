from rest_framework.routers import DefaultRouter
from .views import BlogCategoryViewSet, BlogAuthorViewSet, BlogPostViewSet, PostCommentViewSet

router = DefaultRouter()
router.register(r'categories', BlogCategoryViewSet)
router.register(r'authors', BlogAuthorViewSet)
router.register(r'posts', BlogPostViewSet)
router.register(r'comments', PostCommentViewSet)

urlpatterns = router.urls