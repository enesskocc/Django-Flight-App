from django.db import models


class FixModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # do not create table for this model.


class Flight(FixModel):
    flight_number = models.CharField(max_length=15)
    operation_airlines = models.CharField(max_length=50)
    departure_city = models.CharField(max_length=15)
    arrival_city = models.CharField(max_length=15)
    date_of_departure = models.DateField()
    time_of_departure = models.TimeField()
    # created_time = models.DateTimeField(auto_now_add=True)
    # updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[ {self.flight_number} ] {self.departure_city} -> {self.arrival_city} # {self.date_of_departure} {self.time_of_departure}'


class Passenger(FixModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



from django.contrib.auth.models import User
# related_name = use for call child-models-records from parent-model. (reverse-call)
class Reservation(FixModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='flight_reservations')
    passenger = models.ManyToManyField(Passenger, related_name='passenger_reservations')

    def __str__(self):
        return f'Reservation: {self.flight.flight_number} / Passengers: {self.passenger.count()}'
