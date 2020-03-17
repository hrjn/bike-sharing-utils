def celsius_to_farenheit(temp_c=None):
    """
    Convert temperatures from Celsius to Farenheit
    """

    temp_f = (temp_c * 1.8) + 32
    return temp_f

def convert_wind_speed(w_kmh=None, target_unit=None):
    """
    Convert wind speed from km/h to something else
    """

    w_meters_per_s = w_kmh * 0.27778

    if target_unit == "mph":
        return w_meters_per_s * 2.23694
    elif target_unit == "kts":
        return w_meters_per_s * 0.5924838
    else:
        raise ValueError("Unknown target unit")
