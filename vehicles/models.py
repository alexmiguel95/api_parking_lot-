from django.db import models


class Vehicle(models.Model):
    vehicle_type = models.CharField("Tipo de veículo", max_length=100)
    license_plate = models.CharField("Placa do veículo", max_length=100)
    arrived_at = models.DateTimeField("Entrar do veículo", auto_now_add=True)
    paid_at = models.DateTimeField(
        "Saída do veículo",
        null=True,
        auto_now=True
    )
    amount_paid = models.IntegerField(
        "Quantidade paga",
        null=True,
        default=None
    )

    @property
    def spot(self):
        spot = None

        return spot
