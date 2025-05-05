from question_model import SimpleQuestion
from question_data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    curr_question = SimpleQuestion(question['question'], question['correct_answer'])
    question_bank.append(curr_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz. Your final score was: {quiz.score}/{quiz.question_number}")
