import random

# new_dict = {new_key:new_value for item in list}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student: random.randint(10, 100) for student in names}
print(f"Student scores: {student_scores}")

# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(f"Student scores that pass: {passed_students}")