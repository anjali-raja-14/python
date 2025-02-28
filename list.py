

n = int(input())
students = []

for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

scores = []
for student in students:
    scores.append(student[1])

scores = list(set(scores))
scores.sort()

second_lowest_score = scores[1]

result = []
for student in students:
    if student[1] == second_lowest_score:
        result.append(student[0])

result.sort()
for name in result:
    print(name)
