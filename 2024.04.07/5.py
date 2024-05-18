integer_part = input("Введите целую часть: ")
fractional_part = input("Введите дробную часть: ")

number_miles = float(integer_part + '.' + fractional_part)
number_km = round(number_miles * 1.61, 1)

print(f"{number_miles} миль = {number_km} км")

# Введите целую часть: 15
# Введите дробную часть: 7
# 15.7 миль = 25.3 км


# ИТОГ: отлично — 3/3
