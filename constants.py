G = 9.81
TIME_CONVERSION = 3600
POWER_CONVERSION = 1000
PUMP_TYPES = {
    "1": {"name": "Центробежный", "efficiency": 0.75},
    "2": {"name": "Поршневой", "efficiency": 0.85},
    "3": {"name": "Вихревой", "efficiency": 0.55}
}
HEAD_LIMITS = {
    "low_max": 10,
    "medium_max": 60
}
INPUT_LIMITS = {
    "q": (0.5, 500.0),
    "h": (1.0, 200.0), 
    "p": (800.0, 1200.0)
}