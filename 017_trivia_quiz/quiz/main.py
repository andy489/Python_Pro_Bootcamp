from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

print(logo)
print(f"Quiz contains total {len(question_bank)} questions.")

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
