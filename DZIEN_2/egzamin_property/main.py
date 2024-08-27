from homework import Homework

print("_________ Homework __________")
g = Homework()
g.grade = 93
assert g.grade >= 92
print(f'ocena za projekt: {g.grade}')
