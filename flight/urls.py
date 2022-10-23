# from django.urls import path, include

# urlpatterns = [
# ]

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
# after '/flight/':
router.register('flights', FligthView)
router.register('passengers', PassengerView)
router.register('reservations', ReservationsView)

urlpatterns = router.urls