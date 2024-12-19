from django.urls import path
from .routers import router
from .views.carta_view import CartaCreateAPIView
from .views.poema_view import PoemaCreateAPIView
urlpatterns = [
    path('carta/registro/', CartaCreateAPIView.as_view(), name='cartaregistro'),
    path('poema/registro/', PoemaCreateAPIView.as_view(), name='poemaregistro'),

]

urlpatterns += router.urls
