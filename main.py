from constants import PUMP_TYPES, INPUT_LIMITS
from menu import show_pump_menu
from validation import get_valid_float, get_valid_choice
from operations import calculate_power, get_head_class
from logger import print_and_log

def main():
    print("=== Программа: Напор и мощность насоса ===")
    show_pump_menu()
    pump_choice = get_valid_choice("Ваш выбор: ", PUMP_TYPES.keys())
    pump_name = PUMP_TYPES[pump_choice]["name"]
    efficiency = PUMP_TYPES[pump_choice]["efficiency"]
    print("\n--- Ввод параметров ---")
    q_min, q_max = INPUT_LIMITS["q"]
    q = get_valid_float(f"Подача Q, м³/ч ({q_min}-{q_max}): ", q_min, q_max)
    h_min, h_max = INPUT_LIMITS["h"]
    h = get_valid_float(f"Напор H, м ({h_min}-{h_max}): ", h_min, h_max)
    p_min, p_max = INPUT_LIMITS["p"]
    p = get_valid_float(f"Плотность среды p, кг/м³ ({p_min}-{p_max}): ", p_min, p_max)
    power = calculate_power(p, q, h, efficiency)
    head_class = get_head_class(h)
    print("\n--- Результаты расчета ---")
    print_and_log(f"Тип насоса: {pump_name}")
    print_and_log(f"Подача (Q): {q} м³/ч")
    print_and_log(f"Напор (H): {h} м")
    print_and_log(f"Мощность (P): {power:.2f} кВт")
    print_and_log(f"Класс напора: {head_class}")

if __name__ == "__main__":
    main()