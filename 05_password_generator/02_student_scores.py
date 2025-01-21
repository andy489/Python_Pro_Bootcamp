student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 189, 169, 146]

total_exam_score = sum(student_scores)
print(total_exam_score)

sum_scores = 0
for score in student_scores:
    sum_scores += score

print(sum_scores)

max_exam_score = max(student_scores)
print(max_exam_score)

max_score = -1
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
