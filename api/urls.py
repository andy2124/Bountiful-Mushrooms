from rest_framework.routers import DefaultRouter
from .views import MushroomViewSet

router = DefaultRouter()
router.register('mushrooms', MushroomViewSet, basename = 'mushroom')
urlpatterns = router.urls+[]
