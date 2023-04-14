def round_grades(grades):
    rounded_grades = []  # Создаем пустой список для округленных оценок

    for grade in grades:
        if grade < 40:
            rounded_grade = grade  # Оценка менее 40 не округляется
        elif grade >= 40 and grade < 45:
            rounded_grade = 45  # Оценка 40-44 округляется до 45
        else:
            # Оценка, больше 45, округляется до ближайшего числа, кратного 5
            rounded_grade = round(grade / 5) * 5
        # Добавляем округленную оценку в список
        rounded_grades.append(rounded_grade)

    return rounded_grades


grades = [83, 82, 75, 47, 30, 90]
rounded_grades = round_grades(grades)
print("Оценки до округления:", grades)
print("Оценки после округления:", rounded_grades)
