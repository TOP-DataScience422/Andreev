number = int(input("Введите трехзначное число: "))
first_term = number // 100
second_term = number % 100 // 10
third_term = number % 10
terms_summary = first_term + second_term + third_term
terms_multiplication = first_term * second_term * third_term
print(f"Сумма цифр = {terms_summary}\nПроизведение цифр = {terms_multiplication}")
# Введите трехзначное число: 333
# Сумма цифр = 9
# Произведение цифр = 27