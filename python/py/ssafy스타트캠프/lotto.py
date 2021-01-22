import random

numbers = range(1,46)
# print(numbers)

lucky_numers = random.sample(numbers, 6)
print(sorted(lucky_numers))