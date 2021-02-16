from levels.models import Level
import ipdb


def get_data_level(vehicle_type: str):
    spot_type = "car_spots"

    if vehicle_type != "car":
        spot_type = "bike_spots"

    get_all_level = Level.objects.order_by("fill_priority")

    ipdb.set_trace()
    return get_all_level
