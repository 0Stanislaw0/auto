from rest_framework.routers import DefaultRouter
from .views import CarsView

router = DefaultRouter()
router.register(r'cars', CarsView, basename='api/')
urlpatterns = router.urls
