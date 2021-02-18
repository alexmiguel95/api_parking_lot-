from levels.models import Level
from pricings.models import Pricing


def check_free_space(vehicle_type: str) -> dict:
    all_levels_ordering_the_lowest_fill_priority = Level.objects.order_by(
        "fill_priority"
    )

    # Check if there is a price list
    get_last_price = Pricing.objects.last()

    if all_levels_ordering_the_lowest_fill_priority and get_last_price:

        # Check for available car spaces
        if vehicle_type == "car":
            for level in all_levels_ordering_the_lowest_fill_priority:
                if level.car_spots > 0:
                    level.car_spots -= 1
                    level.save()
                    return {
                        "id": level.pk,
                        "variety": vehicle_type,
                        "level_name": level.name
                    }

        # Check for available bike spaces
        if vehicle_type == "bike":
            for level in all_levels_ordering_the_lowest_fill_priority:
                if level.bike_spots > 0:
                    level.bike_spots -= 1
                    level.save()
                    return {
                        "id": level.pk,
                        "variety": vehicle_type,
                        "level_name": level.name
                    }

    # There are no vacancies or there is no level registered in the system
    return {}
