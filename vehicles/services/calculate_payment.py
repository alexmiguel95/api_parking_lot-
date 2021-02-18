from pricings.models import Pricing
from levels.models import Level
import math


def get_payment(check_in_time, check_out_time, fk_level, vehicle_type) -> int:
    get_last_price = Pricing.objects.last()
    level = Level.objects.get(id=fk_level)
    if vehicle_type == "car":
        level.car_spots += 1
        level.save()

    level.bike_spots += 1
    level.save()

    # Convert to hours
    total_hours = (check_out_time - check_in_time).seconds / 3600
    total_hours = math.ceil(total_hours)

    total_payment = (
        get_last_price.a_coefficient + get_last_price.b_coefficient
    ) * total_hours

    return total_payment
