import random

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() in test}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student: random.randint(10, 100) for student in names}
print(f"Student scores: {student_scores}")

passed_students = {student: score for (student, score) in student_scores.items()}
print(f"Student scores: {passed_students}")


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split(" ")}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

def far(temp_c):
    return temp_c * 9/5 + 32

weather_f = {day:far(temp_c) for (day,temp_c) in weather_c.items()}

print(weather_f)