from constants import G, TIME_CONVERSION, POWER_CONVERSION, HEAD_LIMITS

def calculate_power(p, q, h, efficiency):
    power = (p * G * q * h) / (TIME_CONVERSION * POWER_CONVERSION * efficiency)
    return power

def get_head_class(h):
    if h < HEAD_LIMITS["low_max"]:
        return "Малый напор"
    elif h <= HEAD_LIMITS["medium_max"]:
        return "Средний напор"
    else:
        return "Высокий напор"