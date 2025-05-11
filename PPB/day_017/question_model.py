import json


class SimpleQuestion:

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def to_dict(self):
        return {
            "question": self.question,
            "correct_answer": self.correct_answer,
        }

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __str__(self):
        return self.to_dict()


class Question:

    def __init__(self, category, type_, difficulty, question, correct_answer, incorrect_answers):
        self.category = category
        self.type = type_
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers

    def to_dict(self):
        return {
            "category": self.category,
            "type": self.type,
            "difficulty": self.difficulty,
            "question": self.question,
            "correct_answer": self.correct_answer,
            "incorrect_answers": self.incorrect_answers,
        }

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __str__(self):
        return self.to_dict()
