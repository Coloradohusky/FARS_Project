from rest_framework import routers

from .views import (
    AccidentViewSet,
)

router = routers.DefaultRouter()
router.register(r"accidents", AccidentViewSet)

urlpatterns = router.urls