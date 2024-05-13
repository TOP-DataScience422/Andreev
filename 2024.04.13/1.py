import sys

print("Введите последовательность из чисел. \nКаждое последующее число вводиться через Enter \nДля прекращения ввода введите повторно Enter")
num_array = []
count = 0
for line in sys.stdin:
    line = line.strip('\n')
    if line.strip('-').isnumeric() or line.replace('.','',1).strip('-').isdigit():
        num_array.append(float(line))
        count = count + 1
    else: break
summary = 0
for i in range(count):
	if(num_array[i]) > 0:
		summary = summary + num_array[i]
print(f"Сумма положительных элементов = {summary}")
