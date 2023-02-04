# answer = [num for num in range(1,101) if num % 12 == 0]
# print(answer)

answer = []

for x in range(1,101):
    if x % 12 == 0:
        answer.append(x)
print(answer)