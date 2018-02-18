"""API URLs endpoint for books app """
from rest_framework.routers import DefaultRouter

from .views.books_view import BookViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', BookViewSet)


urlpatterns = router.urls
