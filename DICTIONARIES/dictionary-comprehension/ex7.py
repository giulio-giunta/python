person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
# answer = {person[i][0]: person[i][1] for i in range(0,3)}
# print(answer)

# answer = {k:v for k,v in person}
# print(answer)

answer = dict(person)
print(answer)