from django.db import models


class Level(models.Model):
    name = models.CharField("Nome do piso", max_length=255)
    fill_priority = models.IntegerField("Prioridade de preenchimento")
    bike_spots = models.IntegerField("Quantidade de vagas disponíveis motos")
    car_spots = models.IntegerField("Quantidade de vagas disponíveis carros")

    @property
    def available_spots(self):
        available_spots = {
            "available_bike_spots": self.bike_spots,
            "available_car_spots": self.car_spots
        }

        return available_spots
