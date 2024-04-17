integer_part = input("Введите целую часть: ")
fractional_part = input("Введите дробную часть: ")
numberMiles = float(integer_part + '.' + fractional_part)
numberKm = round(numberMiles * 1.61, 1)
print(f"{numberMiles} миль = {numberKm} км")
# Введите целую часть: 15
# Введите дробную часть: 7
# 15.7 миль = 25.3 км

