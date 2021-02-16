from django.db import models


class Pricing(models.Model):
    a_coefficient = models.IntegerField("Representa o coeficiente linear")
    b_coefficient = models.IntegerField("O coeficiente angular da equação")
