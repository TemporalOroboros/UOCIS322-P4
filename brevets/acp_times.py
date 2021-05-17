"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow



MIN_SPEED = "min_speed" # The minimum speed for a cyclist in the bracket.
MAX_SPEED = "max_speed" # The maximum speed for a cyclist in the bracket.


# The close time 
INITIAL_CLOSE_TIME = 1.0
# 
BRACKETS = {
    0: {MIN_SPEED: 20.0, MAX_SPEED: 34},
    60: {MIN_SPEED: 15.0, MAX_SPEED: 34},
    200: {MIN_SPEED: 15.0, MAX_SPEED: 32},
    400: {MIN_SPEED: 15.0, MAX_SPEED: 30},
    600: {MIN_SPEED: 11.428, MAX_SPEED: 28},
    1000: {MIN_SPEED: 13.333, MAX_SPEED: 26}
}


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    cutoff_dist_km = min(control_dist_km, brevet_dist_km)

    controle_time = 0
    last_bracket_dist_km = 0
    for bracket_dist_km in BRACKETS:
        if bracket_dist_km >= cutoff_dist_km:
            controle_time += (cutoff_dist_km - last_bracket_dist_km) / BRACKETS[last_bracket_dist_km][MAX_SPEED]
            break
        controle_time += (bracket_dist_km - last_bracket_dist_km) / BRACKETS[last_bracket_dist_km][MAX_SPEED]
        last_bracket_dist_km = bracket_dist_km

    return arrow_from_float(brevet_start_time, controle_time)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    cutoff_dist_km = min(control_dist_km, brevet_dist_km)
    
    controle_time = INITIAL_CLOSE_TIME
    last_bracket_dist_km = 0
    for bracket_dist_km in BRACKETS:
        if bracket_dist_km >= cutoff_dist_km:
            controle_time += (cutoff_dist_km - last_bracket_dist_km) / BRACKETS[last_bracket_dist_km][MIN_SPEED]
            break
        controle_time += (bracket_dist_km - last_bracket_dist_km) / BRACKETS[last_bracket_dist_km][MIN_SPEED]
        last_bracket_dist_km = bracket_dist_km

    return arrow_from_float(brevet_start_time, controle_time)


def arrow_from_float(zero_time, hours_as_float):
    """
    Args:
		zero_time: arrow, the time to use as zerowhile constructing the new arrow
        hours_as_float: number, how many hours the 
    Returns:
        An arrow object indicating the 
    """

    hours = hours_as_float // 1
    minutes = round((hours_as_float % 1) * 60)
    return zero_time.shift(hours = hours, minutes = minutes + 0.5).floor('minute')

