answer = ["Elie", "Tim", "Matt"]

answer2 = [ name[0] for name in answer ]

print(answer2)

# answer = [1,2,3,4,5,6]

# answer2 = [ x for x in answer if x % 2 == 0 ]

# print(answer2)

answer = []
for person in ["Elie", "Tim", "Matt"]:
    answer.append(person[0])

answer2 = []
for num in [1,2,3,4,5,6]:
    if num % 2 == 0:
        answer2.append(num)