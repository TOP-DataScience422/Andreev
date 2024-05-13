first_num = int(input())
second_num = int(input())
if(first_num % second_num == 0):
	print(f"{first_num} делится на {second_num} нацело \nчастное: {first_num // second_num}")
else:
	print(f"{first_num} не делится на {second_num} нацело \nнеполное частное: {first_num // second_num} \nостаток: {first_num % second_num}")