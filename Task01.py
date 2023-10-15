"""
Найдите сумму цифр трехзначного числа n
"""

n = 123
sum = 0
for i in str(n):
    sum += int(i)

res = sum
print(res)