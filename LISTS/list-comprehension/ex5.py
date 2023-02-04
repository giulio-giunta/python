# answer = [num for num in [1,2,3,4] if num in [3,4,5,6]]
# print(answer)

# answer2 = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]
# print(answer2)

answer = []
for x in [1,2,3,4]:
    if x in [3,4,5,6]:
        answer.append(x)

answer2 = []
for name in ["Elie", "Tim", "Matt"]:
    answer2.append(name[::-1].lower())

