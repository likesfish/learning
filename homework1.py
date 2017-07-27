numbers = open('numbers.txt').read().strip()
thousands = numbers.split('\n')

for i, integer in enumerate(thousands):
    thousands[i] = int(integer)

maximum = max(thousands)
minimum = min(thousands)
summation = sum(thousands)
average = sum(thousands)/len(thousands)

print(maximum)
print(minimum)
print(summation)
print(average)
