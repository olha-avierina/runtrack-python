def calculate_distance(steps_per_day, step_height_cm):
    # Количество шагов в неделю (учитываем 7 дней)
    steps_per_week = steps_per_day * 7
    distance_per_step_m = step_height_cm / 100  # Высота одной ступеньки в метрах
    total_distance_m = steps_per_week * \
        distance_per_step_m  # Общая дистанция в метрах

    return total_distance_m


steps_per_day = 25  # Количество шагов в день
step_height_cm = 15  # Высота ступеньки в сантиметрах
total_distance_m = calculate_distance(steps_per_day, step_height_cm)
print("За неделю сторож маяка проходит", round(total_distance_m, 2), "метров.")
