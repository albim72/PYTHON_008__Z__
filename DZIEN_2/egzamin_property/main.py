from homework import Homework
from exam import Exam
from grade import ExamG
from weakgrade import ExamD

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

print("_________ ExamG __________")
first = ExamG()
first.math_grade = 34
first.alg_grade = 54
first.prog_grade = 21

print(f'egzamin: matematyka -> {first.math_grade}, '
      f'algorytmika -> {first.alg_grade}, programowanie -> {first.prog_grade}')

sec = ExamG()
sec.math_grade = 56
sec.alg_grade = 76
sec.prog_grade = 71

print(f'egzamin: matematyka -> {sec.math_grade}, '
      f'algorytmika -> {sec.alg_grade}, programowanie -> {sec.prog_grade}')

print("wyniki z archiwum - I termin")
print(f'egzamin: matematyka -> {first.math_grade}, '
      f'algorytmika -> {first.alg_grade}, programowanie -> {first.prog_grade}')

print("_________ ExamD __________")
first = ExamD()
first.math_grade = 34
first.alg_grade = 54
first.prog_grade = 21

print(f'egzamin: matematyka -> {first.math_grade}, '
      f'algorytmika -> {first.alg_grade}, programowanie -> {first.prog_grade}')

sec = ExamD()
sec.math_grade = 56
sec.alg_grade = 76
sec.prog_grade = 71

print(f'egzamin: matematyka -> {sec.math_grade}, '
      f'algorytmika -> {sec.alg_grade}, programowanie -> {sec.prog_grade}')

print("wyniki z archiwum - I termin")
print(f'egzamin: matematyka -> {first.math_grade}, '
      f'algorytmika -> {first.alg_grade}, programowanie -> {first.prog_grade}')
