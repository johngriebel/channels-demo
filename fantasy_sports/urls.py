from rest_framework import routers
from fantasy_sports.views import PlayerViewSet

router = routers.SimpleRouter()
router.register('players', PlayerViewSet)

urlpatterns = router.urls