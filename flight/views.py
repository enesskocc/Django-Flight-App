from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import (
    Flight,
    Passenger,
    Reservation,
)
from .serializers import (
    FlightSerializer,
    PassengerSerializer,
    ReservationSerializer,
)

from .permission import IsStaffPermission

class FligthView(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer#
    permission_classes = [IsStaffPermission]

        # view all details for staff-user:
    def get_serializer_class(self):
        if self.request.user.is_staff:
            # return new serializer:
            from .serializers import StaffFlightSerializer
            return StaffFlightSerializer
        else:
            # return default:
            # return FlightSerializer
            return super().get_serializer_class()


class PassengerView(ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class ReservationsView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
