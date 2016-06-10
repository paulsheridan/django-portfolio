from .views import BlogEntryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'entries', BlogEntryViewSet)
urlpatterns = router.urls

# url(r'^login/', views.obtain_auth_token),
