from homework import Homework
from exam import Exam

print("_________ Homework __________")
g = Homework()
g.grade = 93
assert g.grade >= 92
print(f'ocena za projekt: {g.grade}')

print("_________ Exam __________")
ex= Exam()
ex.part_a_grade = 88
ex.part_b_grade = 73

assert ex.part_a_grade >= 60
assert ex.part_b_grade >= 70

print(f'ocena z egzamin: A -> {ex.part_a_grade}, B -> {ex.part_b_grade}')
