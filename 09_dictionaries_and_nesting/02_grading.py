student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for k in student_scores:

    curr_score = student_scores[k]

    if curr_score >= 91:
        student_grades[k] = "Outstanding"
    elif curr_score >= 81:
        student_grades[k] = "Exceeds Expectations"
    elif curr_score >= 71:
        student_grades[k] = "Acceptable"
    else:
        student_grades[k] = "Fail"

print(student_grades)