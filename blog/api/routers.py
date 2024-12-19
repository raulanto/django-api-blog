from rest_framework.routers import DefaultRouter
from .views.carta_view import CartaViewSet
from .views.user_view import UserViewSet
from .views.poema_view import PoemaViewSet
router = DefaultRouter()
router.register(r'carta', CartaViewSet)
router.register(r'usuarios', UserViewSet)
router.register(r'poema', PoemaViewSet)


